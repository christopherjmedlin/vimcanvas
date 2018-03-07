import pytest
from bson import ObjectId
from vimcanvas.cache import Canvas

@pytest.fixture(scope="function")
def canvas():
    return Canvas("test", ObjectId())

@pytest.mark.parametrize("char,color,x,y,expected_exception", [
    ('@', 'ffffff', 50, 50, 'None'),
    ('a', 'ffffff', 50, 50, 'None'),
    ('5', '000000', 100, 100, 'None'),
    ('#', '00ff00', 550, 550, 'Character coordinates out of bounds.')
])
def test_change_char(canvas, char, color, x, y, expected_exception):
    exception = None
    try:
        canvas.change_char(char, color, x, y)
        assert {
            "char": char,
            "color": color,
            "coords": (x, y)
        } in canvas.altered_chars
    except ValueError as e:
        exception = e
    assert str(exception) == expected_exception

def test_connect(canvas):
    with pytest.raises(Exception) as e:
        #import pdb; pdb.set_trace()
        canvas.connect(1)
    assert str(e.value) == "Handler must be a CanvasWebSocketHandler."
    assert 1 not in canvas.clients

def test_change_char_same_coords(canvas):
    canvas.change_char('#', '00ff00', 50, 50)
    canvas.change_char('@', '000000', 50, 50)
    assert len(canvas.altered_chars) == 1
    assert canvas.altered_chars[0]["coords"] == (50, 50)