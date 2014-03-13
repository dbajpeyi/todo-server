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
        "id": str(todo.id),
    }

class TodoListView(Resource):
    """Get the list of todos"""

    def get(self):
        resp = {'todos': []}
        for todo in Todo.objects():
            resp['todos'].append(todo_as_dict(todo))
        return resp
    
class AddTodoView(Resource):
    """Add this task to db"""

    def post(self):
        args = parser.parse_args()
        todo = Todo(args["task"])
        todo.save()
        return todo_as_dict(todo)

class ToggleTodoStateView(Resource):
    """Toggle the completed flag for this todo"""

    def get(self, id):
        todo = Todo.objects(id=id).first()
        todo.completed = not todo.completed
        todo.save()
        return todo_as_dict(todo)

class ShowTodoView(Resource):
    """Show details corresponding to this todo"""
    
    def get(self, id):
        return todo_as_dict(Todo.objects(id=id).first())

class CompleteAllTodosView(Resource):
    """Mark all tasks as completed"""
    
    def get(self):
        Todo.objects.update(upsert=True, **{"set__completed": True})
        return {"status": "ok"}
