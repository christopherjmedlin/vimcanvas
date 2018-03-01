import tornado
from tornado.web import RequestHandler
from tornado.options import options

import pymongo
from bson import json_util, ObjectId

import json
import hashlib

class HandlerMixin(object):

    @property
    def db(self):
        if not hasattr(self, '_mongo'):
            self._mongo = pymongo.MongoClient(options.mongo_uri)
        return self._mongo.db

    def json_error(self, message):
        self.write('{"error": "{}"}'.format(message))


class CanvasHandler(RequestHandler, HandlerMixin):
    def get(self):
        if (self.get_cookie("user_id")):
            query = {"$or": [{"owner": ObjectId(self.get_cookie("user_id"))},
                             {"active": True}]}
        else:
            query = {"active": True}

        self.write(json_util.dumps(self.db.canvases.find(query)))

    def post(self):
        data = json.loads(self.request.body)
        try:
            data = {
                "title": data["title"],
                "owner": ObjectId(data["owner"]),
                "active": True,
                "alteredCharacters": [],
            }
        except KeyError:
            self.json_error("One of the following fields are missing: title, owner")
        
        if len(data["title"]) > 50:
            self.json_error("Title must be shorter than 50 characters")
        self.db.canvases.insert_one(data)


class UserCreateHandler(RequestHandler, HandlerMixin):
    def post(self):
        data = json.loads(self.request.body)
        