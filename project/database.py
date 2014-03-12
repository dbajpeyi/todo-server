from project import conf
from mongoengine import connect

def db_init():
    params = {
        'db': conf.MONGO_DBNAME,
    }

    db = connect(**params)
    return db
