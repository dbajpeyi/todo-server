# todo-server
[![Build Status](https://travis-ci.org/caulagi/todo-server.png?branch=master)](https://travis-ci.org/caulagi/todo-server)

A simple Flask application that exposes APIs to build
a todo application.  See [todo-client](https://github.com/caulagi/todo-client)
and [todo-setup](https://github.com/caulagi/todo-setup) for
the full thing.

### Setup 

Nope!  You should use [todo-setup](https://github.com/caulagi/todo-setup)

### Setup

Sigh!

        $ mkvirtualenv todo
        $ pip install -r requirements.txt
        $ gunicorn todo.server:app

### Tests

        $ py.test

### License

Licensed under [MIT](https://github.com/caulagi/todo-server/blob/master/LICENSE.mit)
