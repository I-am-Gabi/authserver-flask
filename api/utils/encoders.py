from flask.json import JSONEncoder
from api.db import db
from bson import ObjectId
from datetime import datetime


class CustomJsonEncoder(JSONEncoder):
    def default(self, obj):
        try:
            if isinstance(obj, db.Document):
                return obj.to_mongo()
            if isinstance(obj, datetime):
                return obj.isoformat()
            elif isinstance(obj, ObjectId):
                return str(obj)
            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)
        return JSONEncoder.default(self, obj)
