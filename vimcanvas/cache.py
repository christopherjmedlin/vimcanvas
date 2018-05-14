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

    def remove(self, model_name, obj):
        collection = self._get_collection(model_name)
        collection.remove(obj)
        
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
        self.chars = [[{"char": "_", "color": "00FF00"} for i in range(500)] for j in range(500)]
        self.clients = []

    def change_char(self, char, color, x, y, width=1, height=1):
        try:
            for i in range(y, y + height):
                for j in range(x, x + width):
                    if char:
                        self.chars[i][j]["char"] = char
                    if color:
                        self.chars[i][j]["color"] = color
        except IndexError:
            raise ValueError('Character coordinates out of bounds.')

    @property
    def altered_chars(self):
        altered_chars = []
        for row_index, row in enumerate(self.chars):
            for col_index, char in enumerate(row):
                if char != {"char": "_", "color": "00FF00"}:
                    copy = dict(char)
                    copy["coords"] = (col_index, row_index)
                    altered_chars.append(copy)
        return altered_chars


    def connect(self, handler):
        if type(handler).__name__ != "CanvasWebSocketHandler":
            raise Exception("Handler must be a CanvasWebSocketHandler.")
        self.clients.append(handler)

    def close(self, handler):
        self.clients.remove(handler)

    # firing_handler is incase i want to exclude the handler that sent the 
    # message and prevent echo. it can be left as None if desired
    def write_message(self, message, firing_handler=None):
        for handler in self.clients:
            if handler != firing_handler:
                handler.write_message(message)
                
    def save(self, db):
        db.canvases.update_one({"_id": ObjectId(self._id)},
                               {"altered_chars": self.altered_chars})