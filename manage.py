#!/usr/bin/env python3

import tornado
from tornado.options import parse_command_line, options, define
import tornado.web

from vimcanvas.urls import url_config
from vimcanvas import app

import uuid
import sys
import os

define("secret_key", default=uuid.uuid5)
define("env", default="dev")

if options.env == "prod":
    define("port", default=443)
else:
    define("port", default=8888)

class CommandManager(object):
    """
    Manages a set of commands
    """
    
    def __init__(self, app=None):
        self.app = app
        self._commands = dict()

    def command(self, func):
        """
        Decorator for creating a command
        """
        self._commands[func.__name__] = func

    def set_default_command(self, name):
        self.default_command = name

    def run(self):
        if sys.argv[1]:
            self._commands[sys.argv[1]]()
        else:
            self._commands[self.default_command]()

manager = CommandManager(app)
manager.set_default_command("devserver")

@manager.command
def devserver():
    parse_command_line()
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

@manager.command
def run():
    parse_command_line()
    app.listen(80)
    https_server = tornado.httpserver.HTTPServer(
        app,
        ssl_options = {
            "certfile": os.getenv(
                "SSL_CERT_PATH",
                default=os.path.join("/etc/letsencrypt/live/vimcanvas.christophermedlin.me/", "cert.pem")
            ),
            "keyfile": os.getenv(
                "SSL_KEY_PATH",
                default=os.path.join("/etc/letsencrypt/live/vimcanvas.christophermedlin.me/", "key.pem")
            )
        }
    )
    https_server.listen(443)
    tornado.ioloop.IOLoop.current().start()

def main():
    manager.run()

if __name__ == "__main__":
    main()