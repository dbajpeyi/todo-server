from mongoengine import *
    
class Todo(Document):
    
    activity = StringField(max_length=128, required=True)
    completed = BooleanField(default=False)

    meta = {
        'indexes': ['activity']
    }

    def __str__(self):
        return self.activity

class TodoList(Document):

    title = StringField(required=False)
    todos = ListField(ReferenceField(Todo))

    def __str__(self):
        return self.title
