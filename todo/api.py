"""
todo.api

Expose API for our models
"""
import json
from flask.ext.restful import Resource
from todo.models import Todo

def todo_as_dict(todo):
    return {
        "activity": todo.activity,
        "completed": todo.completed,
    }

class TodoListView(Resource):
    """Get the list of todos"""

    def get(self):
        resp = {'todos': []}
        for todo in Todo.objects():
            resp['todos'].append(todo_as_dict(todo))
        return resp
    
class TodoView(Resource):
    """View to list and update a single todo"""

    def get(self, id):
        return Todo.objects(id=id).first().to_json()
