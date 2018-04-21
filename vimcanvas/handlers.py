import tornado
from tornado.web import RequestHandler
from tornado.options import options

import pymongo
from bson import json_util, ObjectId
from bson.errors import InvalidId

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
        self.write({"error": message})


class BaseHandler(RequestHandler):
    def prepare(self):
        if options.env == 'prod' and self.request.protocol != 'https' and \
           self.request.protocol != 'wss':
            self.redirect('https://' + self.request.host + self.request.path, permanent=True)
        self.add_header("Access-Control-Allow-Origin", "*")


class CanvasHandler(BaseHandler, HandlerMixin):
    def check_origin(self, origin):
        return True

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
                "name": canvas.title
            })
                
        self.write(json.dumps(canvases))

    def post(self):
        data = json.loads(self.request.body)

        try:
            if len(data["title"]) > 50:
                self.json_error("Title must be shorter than 50 characters.")
            else:
                self.cache.insert("canvases", Canvas(data["title"], ObjectId()))
        except KeyError:
            self.json_error("No title was given.")


class CanvasRetrieveHandler(BaseHandler, HandlerMixin):
    def get(self, slug):
        canvas = None
        try:
            canvas = self.cache.get("canvases", ObjectId(slug))
        except InvalidId:
            pass
        if canvas:
            self.write({
                    "_id": str(canvas._id),
                    "name": canvas.title,
                    "alteredChars": canvas.altered_chars
            })
        else:
            self.json_error("Canvas not found.", 404)


class UserCreateHandler(BaseHandler, HandlerMixin):
    def post(self):
        data = json.loads(self.request.body)
        try:
            data = {
                "username": data["username"]
            }
        except KeyError:
            self.json_error("One of the following fields are missing: title, owner")
        