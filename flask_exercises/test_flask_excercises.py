import json
from http import HTTPStatus

from flask import Flask
from flask.testing import FlaskClient

from .flask_excercises import FlaskExercise


def create_flask_client() -> FlaskClient:
    app = Flask(__name__)
    FlaskExercise.configure_routes(app)
    return app.test_client()


class TestFlaskExercise:
    flask_client = create_flask_client()

    def create_user(self, user_data: dict) -> dict:
        response = self.flask_client.post(
            "/user", data=json.dumps(user_data), content_type="application/json"
        )
        assert response.status_code == HTTPStatus.CREATED
        return response.get_json()

    def retrieve_user(self, username: str) -> dict:
        response = self.flask_client.get(f"/user/{username}")
        assert response.status_code == HTTPStatus.OK
        return response.get_json()

    def update_user(self, user_name: str, user_data: dict) -> dict:
        response = self.flask_client.patch(
            f"user/{user_name}",
            data=json.dumps(user_data),
            content_type="application/json",
        )
        assert response.status_code == HTTPStatus.OK
        return response.get_json()

    def delete_user(self, username: str) -> dict:
        response = self.flask_client.delete(f"/user/{username}")
        assert response.status_code == HTTPStatus.NO_CONTENT
        return response.get_json()

    def test_create(self) -> None:
        response = self.create_user({"name": "Heisenberg"})

        assert response == {"data": "User Heisenberg is created!"}

    def test_unprocessable_entity(self) -> None:
        response = self.flask_client.post(
            "/user",
            data=json.dumps({"profession": "Chemistry teacher"}),
            content_type="application/json",
        )

        assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
        assert response.json == {"errors": {"name": "This field is required"}}

    def test_get(self) -> None:
        self.create_user({"name": "Heisenberg"})
        response = self.retrieve_user("Heisenberg")

        assert response == {"data": "My name is Heisenberg"}

    def test_update(self) -> None:
        self.create_user({"name": "Heisenberg"})

        response = self.update_user("Heisenberg", {"name": "Jesse"})
        assert response == {"data": "My name is Jesse"}

    def test_delete(self) -> None:
        self.create_user({"name": "Heisenberg"})
        self.delete_user("Heisenberg")

        response = self.flask_client.get("/user/Heisenberg")
        assert response.status_code == HTTPStatus.NOT_FOUND

    def test_not_found(self) -> None:
        response = self.flask_client.get("/404")
        assert response.status_code == HTTPStatus.NOT_FOUND
