from bson import ObjectId

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Cache(object, metaclass=Singleton):
    
    def initialize(self, model_names):
        self._cache = {}
        for name in model_names:
            self._cache[name] = []
            
    def insert(self, model_name, obj):
        collection = self._get_collection(model_name)
        collection.append(obj)
        
    def get_all(self, model_name):
            return self._get_collection(model_name)
        
    def get(self, model_name, _id):
        for model in self._get_collection(model_name):
            try:
                if model._id == _id:
                    return model
            # ignore exception if object doesn't have id
            except AttributeError:
                pass
        return None

    def _get_collection(self, model_name):
        try:
            return self._cache[model_name]
        except KeyError:
            raise Exception('"' + model_name + '" is not a model name')


class Canvas(object):

    def __init__(self, title, _id):
        self.title = title
        self._id = _id
        self.altered_chars = []
        self.clients = []

    def change_char(self, char, color, x, y):
        if y > 500 or x > 500:
            raise ValueError("Character coordinates out of bounds.")
        # check if there is already an altered char at coordinates
        for altered_char in self.altered_chars:
            if (altered_char["coords"] == (x, y)):
                if char:
                    altered_char["char"] = char
                if color:
                    altered_char["color"] = color
                return
        altered_char = {
            "char": char,
            "color": color,
            "coords": (x, y)
        }
        if not altered_char["char"]:
            altered_char["char"] = '#'
        if not altered_char["color"]:
            altered_char["color"] = '00ff00'
        self.altered_chars.append(altered_char)

    def connect(self, handler):
        if type(handler).__name__ != "CanvasWebSocketHandler":
            raise Exception("Handler must be a CanvasWebSocketHandler.")
        self.clients.append(handler)

    def write_message(self, message):
        for handler in self.clients:
            handler.write_message(message)

    def save(self, db):
        db.canvases.update_one({"_id": ObjectId(self._id)},
                               {"altered_char": self.altered_chars})