from bson import ObjectId

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Canvas(object):

    def __init__(self, name, owner, id):
        self.title = title
        self.owner = owner
        self.id = id
        self.altered_chars = []
        self.clients = []

    def change_char(self, char, color, x, y):
        if y > 500 or x > 500:
            raise Exception("Character coordinates out of bounds.")
        else:
            self.altered_chars += {
                "char": char + "#" + format(color, '06x'),
                "x": x, "y": y
            };
            
    def connect(self, handler):
        self.clients += handler

    def save(self, db):
        db.canvases.update_one({"_id": ObjectId(self.id)},
                               {"altered_char": self.altered_chars})
                               

class Cache(object, metaclass=Singleton):
    
    def __init__(self, model_names):
        self.model_names = model_names
        self.cache = []
        for name in self.model_names:
            self.cache[name] = []
            
    def insert(self, model_name, obj):
        self.cache[model_name] += obj
        
    def get_all(self, model_name):
        return self.cache[model_name]
        
    def get(self, model_name, _id):
        for model in self.cache[model_name]:
            if model._id == _id:
                return model