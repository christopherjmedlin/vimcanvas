"""
This file is for mapping URLs to handlers.
"""

from . import handlers, sockets

url_config = [
    (r"/api/v1/canvases", handlers.CanvasHandler),
    (r"/api/v1/canvases/([^/]+)", handlers.CanvasRetrieveHandler),
    (r"/api/v1/socket", sockets.CanvasWebSocketHandler)
]