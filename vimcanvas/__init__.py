import uuid

import pymongo
from bson import ObjectId

import tornado
from tornado.options import define, options

define("secret_key", default=uuid.uuid5)
define("mongo_uri", default="mongodb://localhost:27017/test")

CACHE_MODELS = [
    "canvases"
]

def make_app():
    from .cache import Cache; Cache().initialize(CACHE_MODELS)
    from .urls import url_config

    return tornado.web.Application(url_config,
        cookie_secret=options.secret_key,
        xsrf_cookies=True,
    )

app = make_app()
