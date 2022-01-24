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

    def create_user(self, user_data: dict):
        response = self.flask_client.post(
            "/user", data=json.dumps(user_data), content_type="application/json"
        )
        assert response.status_code == HTTPStatus.CREATED
        return response.get_json()

    def retrieve_user(self, username: str):
        response = self.flask_client.get(f"/user/{username}")
        assert response.status_code == HTTPStatus.OK
        return response.get_json()

    def update_user(self, user_data: dict):
        response = self.flask_client.patch(
            f"user/{user_data['username']}",
            data=json.dumps(user_data),
            content_type="application/json",
        )
        assert response.status_code == HTTPStatus.OK
        return response.get_json()

    def delete_user(self, username: str):
        response = self.flask_client.delete(f"/user/{username}")
        assert response.status_code == HTTPStatus.NO_CONTENT
        return response.get_json()

    def test_create(self, flask_client: FlaskClient) -> None:
        response = self.create_user({"name": "Heisenberg"})

        assert response == {"data": "User Heisenberg is created!"}

    def test_unprocessable_entity(self, flask_client: FlaskClient) -> None:
        response = self.create_user({"profession": "Chemistry teacher"})

        assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
        assert response == {"errors": {"name": "This field is required"}}

    def test_get(self, flask_client: FlaskClient) -> None:
        self.create_user({"name": "Heisenberg"})
        response = self.retrieve_user("Heisenberg")

        assert response == {"data": {"My name is Heisenberg"}}

    def test_update(self, flask_client: FlaskClient) -> None:
        self.create_user({"name": "Heisenberg"})

        response = self.update_user({"name": "Jesse"})
        assert response == {"data": {"My name is Jesse"}}

    def test_delete(self, flask_client: FlaskClient) -> None:
        self.create_user({"name": "Heisenberg"})
        self.delete_user("Heisenberg")

        response = flask_client.get("/user/Heisenberg")
        assert response.status_code == HTTPStatus.NOT_FOUND

    def test_not_found(self, flask_client: FlaskClient) -> None:
        response = flask_client.get("/404")
        assert response.status_code == HTTPStatus.NOT_FOUND
