import os

MONGO_DBNAME = os.environ.get("MONGDO_DBNAME") or "todo"
ROOT = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')
