import tornado
from tornado.web import RequestHandler
from tornado.options import options

import pymongo
from bson import json_util, ObjectId

import json
import hashlib

from vimcanvas.cache import Cache

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
        canvases = []
        query = {"$or": [
            {"owner": ObjectId(self.get_cookie("user_id"))},
            {"active": False}
        ]}
        inactive_canvases = self.db.find(query)
        
        if len(inactive_canvases):
            for canvas in inactive_canvases:
                canvases += {
                    "_id": canvas._id,
                    "name": canvas.name
                }
        for canvas in Cache().get_all("canvases"):
            canvases += {
                "_id": canvas.db_id,
                "name": canvas.name
            }
                
        self.write(canvases)

    def post(self):
        data = json.loads(self.request.body)
        try:
            data = {
                "_id": ObjectId(),
                "title": data["title"],
                "owner": ObjectId(data["owner"]),
                "active": True,
                "alteredCharacters": []
            }
        except KeyError:
            self.json_error("One of the following fields are missing: title, owner")
        
        if len(data["title"]) > 50:
            self.json_error("Title must be shorter than 50 characters")
        Cache().insert("canvases", data)


class CanvasRetrieveHandler(RequestHandler, HandlerMixin):
    def get(self, slug):
        return Cache().get("canvases", ObjectId(slug))


class UserCreateHandler(RequestHandler, HandlerMixin):
    def post(self):
        data = json.loads(self.request.body)
        try:
            data = {
                "username": data["username"]
            }
        except KeyError:
            self.json_error("One of the following fields are missing: title, owner")
        