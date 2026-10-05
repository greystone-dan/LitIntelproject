"""With ENHANCED_AI_MODE off, text typed or uploaded by a user reaches no model and no network."""
import socket

import pytest
from fastapi.testclient import TestClient

from backend import deidentify_names
from backend.main import app


@pytest.fixture
def no_network(monkeypatch):
	def blocked(*_args, **_kwargs):
		raise AssertionError("An outbound network call was attempted")

	monkeypatch.setattr(socket.socket, "connect", blocked)
	monkeypatch.setattr(socket, "create_connection", blocked)


@pytest.fixture
def no_name_model(monkeypatch):
	def fail(*_args, **_kwargs):
		raise AssertionError("The name model was run")

	monkeypatch.setattr(deidentify_names, "detect_names", fail)
	monkeypatch.setattr(deidentify_names, "_load_model", fail)


def test_deidentify_off_skips_the_name_model_but_still_applies_fixed_rules(monkeypatch, no_network, no_name_model):
	monkeypatch.setenv("ENHANCED_AI_MODE", "off")
	response = TestClient(app).post(
		"/api/deidentify",
		data={
			"text": "Maria Lopez emailed maria@example.com on 2020-01-05.",
			"names": "Maria Lopez",
			"auto_names": "true",
		},
	)
	assert response.status_code == 200
	text = response.json()["text"]
	assert "Maria Lopez" not in text and "maria@example.com" not in text


def test_deidentify_page_shows_name_finding_as_off(monkeypatch):
	monkeypatch.setenv("ENHANCED_AI_MODE", "off")
	html = TestClient(app).get("/deidentify").text
	assert 'id="autoNames" disabled' in html
	assert "switched off here" in html


def test_deidentify_page_keeps_name_finding_when_mode_is_local(monkeypatch):
	monkeypatch.setenv("ENHANCED_AI_MODE", "local")
	html = TestClient(app).get("/deidentify").text
	assert 'id="autoNames" checked' in html


def test_research_page_and_api_are_disabled_when_off(monkeypatch, no_network):
	monkeypatch.setenv("ENHANCED_AI_MODE", "off")
	client = TestClient(app)
	page = client.get("/research")
	assert page.status_code == 200
	assert "Research answers are off" in page.text and "<form" not in page.text
	api = client.post("/research", json={"query": "private question"})
	assert api.status_code == 503
