import json
from http import HTTPStatus

import pytest
from flask import Flask
from flask.testing import FlaskClient

from exercises.flask import FlaskExercise


class TestFlaskExercise:
    @pytest.fixture
    def flask_client(self) -> FlaskClient:
        app = Flask(__name__)
        FlaskExercise.configure_routes(app)
        return app.test_client()

    def test_create(self, flask_client: FlaskClient) -> None:
        payload = json.dumps({"name": "Heisenberg"})
        response = flask_client.post("/user", data=payload, content_type="application/json")
        assert response.status_code == HTTPStatus.CREATED
        assert response.get_json() == {"data": "User Heisenberg is created!"}

    def test_unprocessable_entity(self, flask_client: FlaskClient) -> None:
        payload = json.dumps({"profession": "Chemistry teacher"})
        response = flask_client.post("/user", data=payload, content_type="application/json")
        assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
        assert response.get_json() == {"errors": {"name": "This field is required"}}

    def test_get(self, flask_client: FlaskClient) -> None:
        response = flask_client.get("/user/Heisenberg")
        assert response.status_code == HTTPStatus.OK
        assert response.get_json() == {"data": {"My name is Heisenberg"}}

    def test_update(self, flask_client: FlaskClient) -> None:
        payload = json.dumps({"name": "Jesse"})
        response = flask_client.patch(
            "user/Heisenberg", data=payload, content_type="application/json"
        )
        assert response.status_code == HTTPStatus.OK
        assert response.get_json() == {"data": {"My name is Jesse"}}

    def test_delete(self, flask_client: FlaskClient) -> None:
        response = flask_client.delete("/user/Heisenberg")
        assert response.status_code == HTTPStatus.NO_CONTENT

    def test_not_found(self, flask_client: FlaskClient) -> None:
        response = flask_client.get("/404")
        assert response.status_code == HTTPStatus.NOT_FOUND
