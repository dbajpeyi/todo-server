from flask.ext import restful
from todo.models import TodoList, Todo

class TodoListView(restful.Resource):

    def get(self):
        return TodoList.objects.to_json()

class TodoView(restful.Resource):

    def get(self, id):
        return Todo.objects(id=id).first().to_json()
