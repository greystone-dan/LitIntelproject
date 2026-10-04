import ast
import asyncio
from pathlib import Path

import pytest
from fastapi import HTTPException

from backend.deployment_profile import (
    ANALYSIS_POST_PATHS,
    PUBLIC_ENV,
    classify_path,
    get_deployment_profile,
    is_public_data_only,
    require_analysis_allowed,
)


BACKEND_PATH = Path(__file__).resolve().parents[1] / "backend"
ROUTES_PATH = BACKEND_PATH / "routes.py"
MAIN_PATH = BACKEND_PATH / "main.py"


def _post_route_handlers():
    for source_path in BACKEND_PATH.rglob("*.py"):
        if "legacy" in source_path.parts:
            continue
        tree = ast.parse(source_path.read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            for decorator in node.decorator_list:
                if not (
                    isinstance(decorator, ast.Call)
                    and isinstance(decorator.func, ast.Attribute)
                    and isinstance(decorator.func.value, ast.Name)
                    and decorator.func.value.id in {"router", "app"}
                    and decorator.func.attr == "post"
                ):
                    continue
                if not decorator.args or not isinstance(decorator.args[0], ast.Constant):
                    continue
                path = decorator.args[0].value
                positional_args = [*node.args.posonlyargs, *node.args.args]
                args = [*positional_args, *node.args.kwonlyargs]
                positional_defaults = [None] * (len(positional_args) - len(node.args.defaults))
                positional_defaults.extend(node.args.defaults)
                defaults = [*positional_defaults, *node.args.kw_defaults]
                guard_attached = any(
                    arg.arg == "_analysis_allowed"
                    and default is not None
                    and "require_analysis_allowed" in ast.dump(default)
                    for arg, default in zip(args, defaults)
                )
                input_names = {
                    name.id
                    for arg in args
                    if arg.annotation is not None
                    for name in ast.walk(arg.annotation)
                    if isinstance(name, ast.Name)
                }
                has_upload_input = any(
                    default is not None
                    and any(
                        isinstance(part, ast.Name) and part.id == "File"
                        for part in ast.walk(default)
                    )
                    for default in defaults
                )
                form_text_names = {
                    "text", "document", "memo", "brief", "prompt", "content", "source_text"
                }
                has_free_text_form = any(
                    arg.arg in form_text_names
                    and default is not None
                    and any(
                        isinstance(part, ast.Name) and part.id == "Form"
                        for part in ast.walk(default)
                    )
                    for arg, default in zip(args, defaults)
                )
                has_analysis_model = bool(
                    input_names.intersection({"CaseIngestRequest", "ResearchRequest"})
                )
                accepts_analysis_input = (
                    "UploadFile" in input_names
                    or has_upload_input
                    or has_free_text_form
                    or has_analysis_model
                )
                yield source_path, path, accepts_analysis_input, guard_attached


def test_public_data_only_defaults_off(monkeypatch):
    monkeypatch.delenv(PUBLIC_ENV, raising=False)
    assert is_public_data_only() is False
    assert get_deployment_profile()["public_data_only"] is False


def test_flag_accepts_common_on_and_off_values(monkeypatch):
    for value in ("1", "true", "on", "yes"):
        monkeypatch.setenv(PUBLIC_ENV, value)
        assert is_public_data_only() is True
        assert get_deployment_profile()["public_data_only"] is True
    for value in ("", "0", "false", "off"):
        monkeypatch.setenv(PUBLIC_ENV, value)
        assert is_public_data_only() is False


def test_analysis_guard_is_a_noop_when_mode_is_off(monkeypatch):
    monkeypatch.delenv(PUBLIC_ENV, raising=False)
    asyncio.run(require_analysis_allowed())


def test_analysis_guard_rejects_when_mode_is_on(monkeypatch):
    monkeypatch.setenv(PUBLIC_ENV, "true")
    with pytest.raises(HTTPException) as error:
        asyncio.run(require_analysis_allowed())
    assert error.value.status_code == 403
    assert "public-data-only mode" in error.value.detail


def test_public_read_and_search_paths_remain_classified():
    assert classify_path("/health", "GET") == "public-read"
    assert classify_path("/api/deployment-profile", "GET") == "public-read"
    assert classify_path("/data-explorer", "GET") == "public-read"
    assert classify_path("/cases/{case_id}", "GET") == "public-read"
    assert classify_path("/statutes", "GET") == "public-read"
    assert classify_path("/search", "POST") == "public"
    assert classify_path("/search/chunks", "POST") == "public"

    for _, path, _, guard_attached in _post_route_handlers():
        if classify_path(path, "POST") == "public":
            assert not guard_attached, f"public POST {path} must remain available"

    tree = ast.parse(ROUTES_PATH.read_text(encoding="utf-8"))
    expected_gets = {"/api/deployment-profile", "/data-explorer", "/cases/{case_id}", "/statutes"}
    found_gets = set()
    for node in ast.walk(tree):
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        for decorator in node.decorator_list:
            if (
                isinstance(decorator, ast.Call)
                and isinstance(decorator.func, ast.Attribute)
                and isinstance(decorator.func.value, ast.Name)
                and decorator.func.value.id == "router"
                and decorator.func.attr == "get"
                and decorator.args
                and isinstance(decorator.args[0], ast.Constant)
                and decorator.args[0].value in expected_gets
            ):
                path = decorator.args[0].value
                found_gets.add(path)
                assert "require_analysis_allowed" not in ast.dump(node.args), (
                    f"public GET {path} must remain available"
                )
    assert found_gets == expected_gets


def test_every_post_route_is_classified_and_analysis_inputs_are_guarded():
    handlers = list(_post_route_handlers())
    route_paths = {path for _, path, _, _ in handlers}
    assert route_paths
    assert all(classify_path(path, "POST") != "unclassified" for path in route_paths)

    for source_path, path, accepts_analysis_input, guard_attached in handlers:
        if accepts_analysis_input:
            assert path in ANALYSIS_POST_PATHS, (
                f"{source_path}: POST {path} accepts file/free-text analysis input "
                "but is not classified"
            )
            assert guard_attached, (
                f"{source_path}: POST {path} accepts file/free-text analysis input "
                "but lacks the mode guard"
            )

    assert ANALYSIS_POST_PATHS <= route_paths


def test_health_and_profile_handlers_expose_the_active_mode():
    main_tree = ast.parse(MAIN_PATH.read_text(encoding="utf-8"))
    health = next(
        node for node in main_tree.body
        if isinstance(node, ast.FunctionDef) and node.name == "health"
    )
    assert any(
        isinstance(node, ast.Name) and node.id == "get_deployment_profile"
        for node in ast.walk(health)
    )

    routes_tree = ast.parse(ROUTES_PATH.read_text(encoding="utf-8"))
    profile_handler = next(
        node for node in routes_tree.body
        if isinstance(node, ast.FunctionDef) and node.name == "get_deployment_profile_api"
    )
    assert any(
        isinstance(node, ast.Name) and node.id == "get_deployment_profile"
        for node in ast.walk(profile_handler)
    )


def test_analysis_pages_add_the_profile_and_disabled_explanation():
    tree = ast.parse(ROUTES_PATH.read_text(encoding="utf-8"))
    page_handlers = {
        node.name: node
        for node in tree.body
        if isinstance(node, ast.FunctionDef)
    }
    for handler_name in (
        "live_analysis_page",
        "memo_citation_check_page",
        "deidentify_page",
        "research_interface",
    ):
        handler = page_handlers[handler_name]
        assert any(
            isinstance(node, ast.Name) and node.id == "_with_deployment_profile_notice"
            for node in ast.walk(handler)
        ), f"{handler_name} must expose the profile and disabled-mode explanation"
