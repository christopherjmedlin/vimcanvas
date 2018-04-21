import tornado
import tornado.websocket

import random

from vimcanvas import cache
from vimcanvas.handlers import HandlerMixin
from bson import ObjectId

class CanvasWebSocketHandler(tornado.websocket.WebSocketHandler, HandlerMixin):

    @property
    def canvas(self):
        if not hasattr(self, '_canvas'):
            canvas_id = self.get_argument("id")
            self._canvas = self.cache.get("canvases", ObjectId(canvas_id))
        return self._canvas

    def check_origin(self, origin):
        return True

    def open(self):
        self.id = ObjectId()
        self.canvas.connect(self)
        self.canvas.write_message({
            "event": {
                "type": "join",
                "data": {
                    "username": "Anonymous",
                    "id": str(self.id)
                }
            }	
        })
    
    def on_message(self, message):
        self._interpret_command(message)
    
    def on_close(self):
        self.canvas.close(self)
        print("Closed")

    def _interpret_command(self, command):
        command = command.split()
        args = command[1:]
        command = command[0]

        args[0] = int(args[0])
        args[1] = int(args[1])

        if command == 'move':
            self._move(args)
        elif command == 'char':
            self._change_char(args[2], args[0],  args[1])
        elif command == 'color':
            self._change_color(args[2], args[0], args[1])

    def _change_char(self, char, x, y):
        self.canvas.change_char(char, None, x, y)
        self.canvas.write_message({
            "event": {
                "type": "char",
                "data": {
                    "x": x,
                    "y": y,
                    "char": char
                }
            }
        })

    def _change_color(self, color, x, y):
        self.canvas.change_char(None, color, x, y)
        self.canvas.write_message({
            "event": {
                "type": "color",
                "data": {
                    "x": x,
                    "y": y,
                    "color": color
                }
            }
        })

    def _move(self, args):
        self.x = args[0]
        self.y = args[1]

        if self.x <= 100 and self.y <= 100:
            self.canvas.write_message({
                "event": {
                    "type": "move",
                    "data": {
                        "x": self.x,
                        "y": self.y,
                        "id": str(self.id)
                    }
                }
            })