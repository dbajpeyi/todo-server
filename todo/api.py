import json
from flask.ext import restful
from project.instance import app
from todo.models import TodoList, Todo

api = restful.Api(app)

class TodoListView(restful.Resource):
    
    def get(self):
        return Todo.objects.to_json()

class TodoView(restful.Resource):
    
    def get(self, id):
        return Todo.objects(id=id).first().to_json()

api.add_resource(TodoView, '/api/v1/todos/<string:id>')
api.add_resource(TodoListView, '/api/v1/todos')
