"""
This file is for mapping URLs to handlers.
"""

from . import handlers

url_config = [
    (r"/api/v1/canvases", handlers.CanvasHandler)
]