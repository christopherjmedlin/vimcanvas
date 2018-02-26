import tornado

class GameWebSocket(tornado.websocket.WebSocketHandler):
    def open(self):
        print("opened")
    
    def on_message(self, message):
        self.write_message("asdf")
    
    def on_close(self):
        print("Closed")