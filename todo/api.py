"""
todo.api

Expose API for our models
"""
from flask.ext.restful import Resource
from todo.models import Todo

class TodoListView(Resource):
    """View to list all todos"""

    def get(self):
        return Todo.objects().to_json()
    
class TodoView(Resource):
    """View to list and update a single todo"""

    def get(self, id):
        return Todo.objects(id=id).first().to_json()
