"""
project.routes

Bind the api's to the endpoints
"""
from flask.ext.restful import Api
from todo.api import *

def routes_init(app):
    api = Api(app)

    api.add_resource(TodoListView, "/api/v1/todos")
    api.add_resource(AddTodoView, "/api/v1/todos/add")
    api.add_resource(ToggleTodoStateView, "/api/v1/todos/<string:id>/toggle")
    api.add_resource(ShowTodoView, "/api/v1/todos/<string:id>")

    return api
