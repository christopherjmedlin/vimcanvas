import tornado
from tornado.web import RequestHandler
from tornado.options import options

import pymongo

class BaseRequestHandler(tornado.web.RequestHandler):

    @property
    def db(self):
        if not hasattr(self, '_db'):
            self._db = pymongo.MongoClient(options.mongo_uri)
        return self._db

class CanvasHandler(BaseRequestHandler):
    def get(self):
        