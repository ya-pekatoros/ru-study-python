from flask import Flask, request
import json


class FlaskExercise:
    """
    Вы должны создать API для обработки CRUD запросов.
    В данной задаче все пользователи хранятся в одном словаре, где ключ - это имя пользователя,
    а значение - его параметры. {"user1": {"age": 33}, "user2": {"age": 20}}
    Словарь (dict) хранить в памяти, он должен быть пустым при старте flask.

    POST /user - создание пользователя.
    В теле запроса приходит JSON в формате {"name": <имя пользователя>}.
    Ответ должен вернуться так же в JSON в формате {"data": "User <имя пользователя> is created!"}
    со статусом 201.
    Если в теле запроса не было ключа "name", то в ответ возвращается JSON
    {"errors": {"name": "This field is required"}} со статусом 422

    GET /user/<name> - чтение пользователя
    В ответе должен вернуться JSON {"data": "My name is <name>"}. Статус 200

    PATCH /user/<name> - обновление пользователя
    В теле запроса приходит JSON в формате {"name": <new_name>}.
    В ответе должен вернуться JSON {"data": "My name is <new_name>"}. Статус 200

    DELETE /user/<name> - удаление пользователя
    В ответ должен вернуться статус 204
    """

    @staticmethod
    def configure_routes(app: Flask) -> None:
        users = {}

        @app.route(
            "/user",
            methods=[
                "POST",
            ],
        )
        def create_user():  # type: ignore
            user_name = request.get_json().get("name")
            if user_name:
                users[user_name] = {}
                data = {"data": f"User {user_name} is created!"}
                response = app.response_class(
                    response=json.dumps(data), status=201, mimetype="application/json"
                )
                return response
            data = {"errors": {"name": "This field is required"}}
            response = app.response_class(
                response=json.dumps(data), status=422, mimetype="application/json"
            )
            return response

        @app.route("/user/<name>", methods=["GET", "PATCH", "DELETE"])
        def user(name):  # type: ignore
            if request.method == "GET":
                if name in users:
                    data = {"data": f"My name is {name}"}
                    response = app.response_class(
                        response=json.dumps(data), status=200, mimetype="application/json"
                    )
                    return response
                return "Not found", 404
            if request.method == "PATCH":
                if name in users:
                    new_user_name = request.get_json().get("name")
                    users[new_user_name] = users[name]
                    del users[name]
                    data = {"data": f"My name is {new_user_name}"}
                    response = app.response_class(
                        response=json.dumps(data), status=200, mimetype="application/json"
                    )
                    return response
                return "Not found", 404
            if request.method == "DELETE":
                if name in users:
                    del users[name]
                    return "Sucess deleting", 204
                return "Not found", 404
