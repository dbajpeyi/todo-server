from project import conf
from project.instance import app
from mongoengine import connect

params = {
    'db': conf.MONGO_DBNAME,
}

db = connect(**params)
