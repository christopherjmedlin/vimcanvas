import tornado
from tornado.web import RequestHandler
from tornado.options import options

import pymongo
from bson import json_util, ObjectId

import json
import hashlib

from vimcanvas.cache import Cache, Canvas

class HandlerMixin(object):

    @property
    def db(self):
        if not hasattr(self, '_mongo'):
            self._mongo = pymongo.MongoClient(options.mongo_uri)
        return self._mongo.db

    @property
    def cache(self):
        if not hasattr(self, '_cache'):
            self._cache = Cache()
        return self._cache

    def json_error(self, message, status=400):
        self.set_status(status)
        self.write('{"error": "{}"}'.format(message))


class CanvasHandler(RequestHandler, HandlerMixin):
    def get(self):
        canvases = []

        # query = {"$or": [
        #     {"owner": ObjectId(self.get_cookie("user_id"))},
        #     {"active": False}
        # ]}
        #
        # inactive_canvases = self.db.find(query)
        #
        # if len(inactive_canvases):
        #     for canvas in inactive_canvases:
        #         canvases += {
        #             "_id": canvas._id,
        #             "name": canvas.name
        #         }

        for canvas in self.cache.get_all("canvases"):
            canvases.append({
                "_id": str(canvas._id),
                "name": canvas.title,
                "alteredChars": canvas.altered_chars
            })
                
        self.write(json.dumps(canvases))

    def post(self):
        import pdb; pdb.set_trace()
        data = json.loads(self.request.body)

        if len(data["title"]) > 50:
            self.json_error("Title must be shorter than 50 characters.")
        try:
            self.cache.insert("canvases", Canvas(data["title"], ObjectId()))
        except KeyError:
            self.json_error("No title was given.")


class CanvasRetrieveHandler(RequestHandler, HandlerMixin):
    def get(self, slug):
        self.write(self.cache.get("canvases", ObjectId(slug)))


class UserCreateHandler(RequestHandler, HandlerMixin):
    def post(self):
        data = json.loads(self.request.body)
        try:
            data = {
                "username": data["username"]
            }
        except KeyError:
            self.json_error("One of the following fields are missing: title, owner")
        