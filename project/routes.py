"""
project.routes

Bind the api's to the endpoints
"""
from flask.ext.restful import Api
from todo.api import TodoListView, AddTodoView

def routes_init(app):
    api = Api(app)

    api.add_resource(TodoListView, "/api/v1/todos")
    api.add_resource(AddTodoView, "/api/v1/todos/add")

    return api
