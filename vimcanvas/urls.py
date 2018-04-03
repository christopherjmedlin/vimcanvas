"""
This file is for mapping URLs to handlers.
"""

from . import handlers, sockets

url_config = [
    (r"/v1/canvases", handlers.CanvasHandler),
    (r"/v1/canvases/([^/]+)", handlers.CanvasRetrieveHandler),
    (r"/v1/socket", sockets.CanvasWebSocketHandler)
]