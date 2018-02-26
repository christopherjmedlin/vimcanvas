from bson import ObjectId

class CanvasBuffer(object):

    def __init__(self, name, owner, db_id):
        self.name = name
        self.owner = owner
        self.db_id = db_id
        self.altered_chars = []

    def change_char(self, char, color, x, y):
        if y > 500 or x > 500:
            raise Exception("Character coordinates out of bounds.")
        else:
            self.altered_chars += {
                "char": char + "#" + format(color, '06x'),
                "x": x, "y": y
            };

    def save(self, db):
        db.canvases.update_one({"_id": ObjectId(self.db_id)},
                               {"altered_char": self.altered_chars})