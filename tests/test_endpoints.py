import pytest
import json
from bson import ObjectId

from tornado.httpclient import HTTPRequest, HTTPError

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
    response = yield http_client.fetch(base_url + "/v1/canvases")
    assert response.code == 200
    response = json.loads(response.body)
    assert len(response) == 3

@pytest.mark.gen_test
@pytest.mark.parametrize("post,expected_code,expected_error", [
    ({"title": "Test1"}, 200, "None"),
    ({}, 400, "No title was given."),
    ({"title": TITLE_TOO_LONG}, 400, "Title must be shorter than 50 characters."),
])
def test_canvas_post(http_client, base_url, post, expected_code, expected_error):
    request = HTTPRequest(base_url + "/v1/canvases",
        method="POST",
        body=json.dumps(post)
    )
    if expected_code != 200:
        with pytest.raises(HTTPError) as err:
            yield http_client.fetch(request)
        assert str(expected_code) in str(err.value)
    else:
        response = yield http_client.fetch(request)
        assert response.code == expected_code

@pytest.mark.gen_test
def test_canvas_post_same_title(http_client, base_url):
    request = HTTPRequest(base_url + "/v1/canvases",
        method="POST",
        body='{"title": "Test1"}'
    )
    response = yield http_client.fetch(request)
    assert response.code == 200
    with pytest.raises(HTTPError) as err:
        yield http_client.fetch(request)
    assert "400" in str(err.value)

@pytest.mark.gen_test
def test_canvas_retrieve(http_client, base_url):
    populate()
    response = yield http_client.fetch(base_url + "/v1/canvases/5a9d4f10575e225241d8ebc8")
    assert json.loads(response.body)["name"] == 'Test1'
    with pytest.raises(HTTPError) as err:
        yield http_client.fetch(base_url + "/v1/canvases/nonexistantobject")
    assert "404" in str(err.value)