"""
todo.api

Expose API for our models
"""
import json
from flask.ext.restful import reqparse, Resource
from todo.models import Todo

parser = reqparse.RequestParser()
parser.add_argument('task', type=str)

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
    
class AddTodoView(Resource):
    """View to list and update a single todo"""

    def post(self):
        args = parser.parse_args()
        todo = Todo(args["task"])
        todo.save()
        return todo_as_dict(todo)
