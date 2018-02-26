#!/usr/bin/env python

import tornado
from tornado.options import parse_command_line, options, define
import tornado.web

from vimcanvas.urls import url_config
from vimcanvas import app

import uuid
import sys

define("secret_key", default=uuid.uuid5)
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

@manager.command
def runserver():
    parse_command_line()
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

def main():
    manager.run()

if __name__ == "__main__":
    main()