import pytest
from unittest import mock

from bson import ObjectId

from vimcanvas import CACHE_MODELS
from vimcanvas.cache import Cache, Canvas
from vimcanvas.sockets import CanvasWebSocketHandler

@pytest.fixture(scope="function")
def cache():
    cache = Cache()
    # re initialize after every function
    cache.initialize(CACHE_MODELS)
    cache._cache["canvases"] = [2, 3, 4]
    return cache

@pytest.mark.parametrize("model_names,expected_cache", [
    (["model"], {"model": []}),
    (["model1", "model2"], {"model1": [], "model2": []}),
    ([], {})
])
def test_initialize(cache, model_names, expected_cache):
    cache.initialize(model_names)
    assert cache._cache == expected_cache

@pytest.mark.parametrize("model,expected_exception,expected_result", [
    ("canvases", "None", [2, 3, 4]),
    ("nothing", '"nothing" is not a model name', None),
    ("", '"" is not a model name', None)
])
def test_get_all(cache, model, expected_exception, expected_result):
    exception = None
    try:
        result = cache.get_all(model)
        assert result == expected_result
    except Exception as e:
        exception = e
    assert str(exception) == expected_exception

def test_get(cache):
    _id = ObjectId('5a9d217f575e223270a8dad3')
    canvas = Canvas("Test", _id)
    cache._cache["canvases"].append(canvas)
    assert cache.get("canvases", _id) == canvas
    assert cache.get("canvases", ObjectId()) == None

def test_insert(cache):
    cache.insert("canvases", 1)
    assert 1 in cache._cache["canvases"]