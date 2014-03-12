"""
project.database

Simple module that connects to mongo database and returns the
connection
"""
from project import conf
from mongoengine import connect

def db_init():
    """Connect to database and return the connection"""
    params = {
        'db': conf.MONGO_DBNAME,
    }

    db = connect(**params)
    return db
