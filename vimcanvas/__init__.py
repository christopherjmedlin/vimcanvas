import uuid

import tornado
from tornado.options import define, options

from .urls import url_config
from .database import init_db

define("secret_key", default=uuid.uuid5)

def make_app():
    return tornado.web.Application(url_config,
        cookie_secret=options.secret_key,
        xsrf_cookies=True,
    )

app = make_app()
init_db()
