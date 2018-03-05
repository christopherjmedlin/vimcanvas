import pytest
import json
from bson import ObjectId

from tornado.httpclient import HTTPRequest

from vimcanvas import make_app
from vimcanvas.cache import Cache, Canvas

TITLE_TOO_LONG = ""
for i in range(51):
    TITLE_TOO_LONG += "a"

def populate():
    cache = Cache()
    canvas = Canvas("Test1", ObjectId('5a9d4f10575e225241d8ebc8'))
    canvas.change_char('@', 'ffffff', 50, 50)
    canvas.change_char('@', 'ffff00', 50, 50)
    canvas.change_char('&', 'ffff00', 110, 50)
    canvas.change_char(')', '000000', 50, 60)
    cache.insert("canvases", canvas)
    canvas = Canvas("Test2", ObjectId())
    canvas.change_char('&', 'ffff00', 110, 50)
    cache.insert("canvases", canvas)
    canvas = Canvas("Test3", ObjectId())
    cache.insert("canvases", canvas)

@pytest.fixture
def app():
    return make_app()

@pytest.mark.gen_test
def test_canvas_list(http_client, base_url):
    populate()
    response = yield http_client.fetch(base_url + "/api/v1/canvases")
    assert response.code == 200
    response = json.loads(response.body)
    assert len(response) == 3
    assert len(response[0]["alteredChars"]) == 3

@pytest.mark.gen_test
@pytest.mark.parametrize("post,expected_code,expected_error", [
    ({"title": "Test1"}, 200, "None"),
    ({}, 400, "No title was given."),
    ({"title": TITLE_TOO_LONG}, 400, "Title must be shorter than 50 characters.")
])
def test_canvas_post(http_client, base_url, post, expected_code, expected_error):
    response = yield http_client.fetch(HTTPRequest(base_url + "/api/v1/canvases",
                                                   method="POST",
                                                   body=json.dumps(post)))
    import pdb; pdb.set_trace()