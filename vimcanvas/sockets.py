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
        self.x = random.randrange(0, 500)
        self.y = random.randrange(0, 500)
    
    def on_message(self, message):
        self._interpret_command(message)
    
    def on_close(self):
        self.canvas.close(self)
        print("Closed")

    def _interpret_command(self, command):
        command = command.split()
        args = command[1:]
        command = command[0]

        if command == 'move':
            self._move(args)
        elif command == 'char':
            self.canvas.change_char(args[2], None, args[0],  args[1])
        elif command == 'color':
            self.canvas.change_char(None, args[2], args[0], args[1])

    def _move(self, args):
        self.x = args[0]
        self.y = args[1]
            
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