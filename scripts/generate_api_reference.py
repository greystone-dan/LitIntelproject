"""Generate the checked-in API appendix from the FastAPI OpenAPI schema."""

from __future__ import annotations

import argparse
import inspect
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from fastapi.routing import APIRoute

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
	sys.path.insert(0, str(PROJECT_ROOT))

DEFAULT_OUTPUT = PROJECT_ROOT / "docs" / "API_REFERENCE.generated.md"
HTTP_METHODS = ("get", "post", "put", "patch", "delete", "head", "options")


def _schema_label(schema: dict[str, Any] | None) -> str:
	if not schema:
		return "unspecified"
	if "$ref" in schema:
		return str(schema["$ref"]).rsplit("/", 1)[-1]
	if "type" in schema:
		return str(schema["type"])
	if "anyOf" in schema:
		return " | ".join(_schema_label(item) for item in schema["anyOf"])
	return "inline schema"


def _json_value(value: Any) -> str:
	return json.dumps(value, ensure_ascii=True, separators=(",", ":"))


def _render_parameter(parameter: dict[str, Any]) -> str:
	name = parameter.get("name", "unnamed")
	location = parameter.get("in", "unknown")
	required = "required" if parameter.get("required") else "optional"
	schema = parameter.get("schema") or {}
	detail = _schema_label(schema)
	if "default" in schema:
		detail += f", default `{_json_value(schema['default'])}`"
	if "enum" in schema:
		detail += ", values " + ", ".join(f"`{value}`" for value in schema["enum"])
	description = str(parameter.get("description") or "").strip()
	line = f"- `{name}` ({location}, {required}; {detail})"
	return f"{line}: {description}" if description else line


def _render_operation(path: str, method: str, operation: dict[str, Any]) -> list[str]:
	lines = [f"### `{method.upper()} {path}`", ""]
	summary = str(operation.get("summary") or operation.get("operationId") or "").strip()
	description = str(operation.get("description") or "").strip()
	if summary:
		lines.extend([summary, ""])
	if description and description != summary:
		lines.extend([description, ""])
	if operation.get("deprecated"):
		lines.extend(["**Deprecated.**", ""])
	parameters = operation.get("parameters") or []
	if parameters:
		lines.extend(["**Parameters**", ""])
		lines.extend(_render_parameter(parameter) for parameter in parameters)
		lines.append("")
	request_body = operation.get("requestBody")
	if request_body:
		required = "required" if request_body.get("required") else "optional"
		lines.extend([f"**Request body ({required})**", ""])
		for content_type, content in sorted((request_body.get("content") or {}).items()):
			lines.append(f"- `{content_type}`: `{_schema_label(content.get('schema'))}`")
		lines.append("")
	responses = operation.get("responses") or {}
	lines.extend(["**Responses**", ""])
	for status, response in sorted(responses.items(), key=lambda item: item[0]):
		description = str(response.get("description") or "").strip()
		content = response.get("content") or {}
		if content:
			content_labels = "; ".join(
				f"`{content_type}`: `{_schema_label(value.get('schema'))}`"
				for content_type, value in sorted(content.items())
			)
			lines.append(f"- `{status}`: {description or 'response'}; {content_labels}")
		else:
			lines.append(f"- `{status}`: {description or 'response'}")
	lines.append("")
	return lines


def _render_hidden_route(route: APIRoute, method: str) -> list[str]:
	lines = [f"### `{method.upper()} {route.path}`", "", "**Hidden from OpenAPI.**", ""]
	handler = f"{route.endpoint.__module__}.{route.endpoint.__name__}"
	lines.extend([f"Handler: `{handler}`", ""])
	parameters = list(inspect.signature(route.endpoint).parameters.values())
	if parameters:
		lines.extend(["**Handler parameters**", ""])
		for parameter in parameters:
			annotation = (
				parameter.annotation.__name__
				if hasattr(parameter.annotation, "__name__")
				else str(parameter.annotation).replace("typing.", "")
			)
			default = "required" if parameter.default is inspect.Parameter.empty else f"default `{parameter.default!r}`"
			lines.append(f"- `{parameter.name}` ({annotation}; {default})")
		lines.append("")
	lines.extend([
		"**Responses**",
		"",
		"- Not declared in OpenAPI; inspect the route handler or exercise the endpoint for the current response contract.",
		"",
	])
	return lines


def render_openapi_reference(schema: dict[str, Any], hidden_routes: list[APIRoute]) -> str:
	info = schema.get("info") or {}
	paths = schema.get("paths") or {}
	operations = [
		(path, method, operation)
		for path, path_item in sorted(paths.items())
		for method, operation in sorted(path_item.items())
		if method in HTTP_METHODS
	]
	hidden_operations = [
		(route, method.lower())
		for route in hidden_routes
		for method in sorted(route.methods or set())
		if method.lower() in HTTP_METHODS
	]
	lines = [
		"# Generated API Reference",
		"",
		"This file is generated from `backend.main:app.openapi()` by "
		"`scripts/generate_api_reference.py`. Do not edit it manually.",
		"",
		f"Generated: {datetime.now(timezone.utc).isoformat()}",
		f"OpenAPI title: {info.get('title', 'FastAPI')}",
		f"OpenAPI version: {info.get('version', 'unspecified')}",
		f"OpenAPI operations: {len(operations)} across {len(paths)} paths",
		f"Hidden operations: {len(hidden_operations)} excluded from OpenAPI",
		"",
		"The live OpenAPI UI is available at `/docs`. This appendix records the "
		"route contract present when it was generated. Request/response component "
		"definitions remain available in the live schema. Routes deliberately hidden "
		"from OpenAPI are appended with their handler signature.",
		"",
		"## Operations",
		"",
	]
	for path, method, operation in operations:
		lines.extend(_render_operation(path, method, operation))
	if hidden_operations:
		lines.extend(["## Hidden Operations", ""])
		for route, method in sorted(hidden_operations, key=lambda item: (item[0].path, item[1])):
			lines.extend(_render_hidden_route(route, method))
	return "\n".join(lines).rstrip() + "\n"


def main() -> None:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
	args = parser.parse_args()

	from backend.main import app

	output = args.output.resolve()
	output.parent.mkdir(parents=True, exist_ok=True)
	hidden_routes = [route for route in app.routes if isinstance(route, APIRoute) and not route.include_in_schema]
	output.write_text(render_openapi_reference(app.openapi(), hidden_routes), encoding="utf-8")
	print(f"generated={output}")


if __name__ == "__main__":
	main()