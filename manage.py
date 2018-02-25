import tornado
from tornado.options import parse_command_line, options, define
import tornado.web

from vimcanvas.urls import url_config
import uuid

define("secret_key", default=uuid.uuid5)

def make_app():
    return tornado.web.Application(url_config,
        cookie_secret=options.secret_key,
        xsrf_cookies=True,
    )

def main():
    parse_command_line()
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()