"""
project.routes

Bind the api's to the endpoints
"""
from flask.ext.restful import Api
from todo.api import TodoListView, TodoView

def routes_init(app):
    api = Api(app)

    api.add_resource(TodoListView, "/api/v1/todos")
    api.add_resource(TodoView, "/api/v1/todos/<string:id>")

    return api
