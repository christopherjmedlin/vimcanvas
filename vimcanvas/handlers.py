import tornado
from tornado.web import RequestHandler
from tornado.options import options

import pymongo
from bson import json_util

class DatabaseMixin(object):

    @property
    def db(self):
        if not hasattr(self, '_mongo'):
            self._mongo = pymongo.MongoClient(options.mongo_uri)
        return self._mongo.db

class CanvasHandler(RequestHandler, DatabaseMixin):
    def get(self):
        if (self.get_cookie("user_id")):
            query = {"$or": [{"owner": self.get_cookie("user_id")},
                             {"active": True}]}
        else:
            query = {"active": True}

        self.write(json_util.dumps(self.db.canvases.find(query)))