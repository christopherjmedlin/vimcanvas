{"changed":true,"filter":false,"title":"data.py","tooltip":"/vimcanvas/data.py","value":"from bson import ObjectId\n\nclass Cache(object):\n\n    def __init__(self, name, owner, db_id):\n        self.title = title\n        self.owner = owner\n        self.db_id = db_id\n        self.altered_chars = []\n        self.clients = []\n\n    def change_char(self, char, color, x, y):\n        if y > 500 or x > 500:\n            raise Exception(\"Character coordinates out of bounds.\")\n        else:\n            self.altered_chars += {\n                \"char\": char + \"#\" + format(color, '06x'),\n                \"x\": x, \"y\": y\n            };\n            \n    def connect(self, handler):\n        self.clients += handler\n\n    def save(self, db):\n        db.canvases.update_one({\"_id\": ObjectId(self.db_id)},\n                               {\"altered_char\": self.altered_chars})","undoManager":{"mark":93,"position":100,"stack":[[{"start":{"row":20,"column":16},"end":{"row":20,"column":17},"action":"insert","lines":["s"],"id":350}],[{"start":{"row":20,"column":17},"end":{"row":20,"column":18},"action":"insert","lines":["l"],"id":351}],[{"start":{"row":20,"column":17},"end":{"row":20,"column":18},"action":"remove","lines":["l"],"id":352}],[{"start":{"row":20,"column":17},"end":{"row":20,"column":18},"action":"insert","lines":["e"],"id":353}],[{"start":{"row":20,"column":18},"end":{"row":20,"column":19},"action":"insert","lines":["l"],"id":354}],[{"start":{"row":20,"column":19},"end":{"row":20,"column":20},"action":"insert","lines":["f"],"id":355}],[{"start":{"row":20,"column":20},"end":{"row":20,"column":21},"action":"insert","lines":[","],"id":356}],[{"start":{"row":20,"column":21},"end":{"row":20,"column":22},"action":"insert","lines":[" "],"id":357}],[{"start":{"row":20,"column":22},"end":{"row":20,"column":23},"action":"insert","lines":["h"],"id":358}],[{"start":{"row":20,"column":23},"end":{"row":20,"column":24},"action":"insert","lines":["a"],"id":359}],[{"start":{"row":20,"column":24},"end":{"row":20,"column":25},"action":"insert","lines":["n"],"id":360}],[{"start":{"row":20,"column":25},"end":{"row":20,"column":26},"action":"insert","lines":["d"],"id":361}],[{"start":{"row":20,"column":26},"end":{"row":20,"column":27},"action":"insert","lines":["l"],"id":362}],[{"start":{"row":20,"column":27},"end":{"row":20,"column":28},"action":"insert","lines":["e"],"id":363}],[{"start":{"row":20,"column":28},"end":{"row":20,"column":29},"action":"insert","lines":["r"],"id":364}],[{"start":{"row":20,"column":30},"end":{"row":20,"column":31},"action":"insert","lines":[":"],"id":365}],[{"start":{"row":20,"column":31},"end":{"row":20,"column":32},"action":"insert","lines":["s"],"id":366}],[{"start":{"row":20,"column":31},"end":{"row":20,"column":32},"action":"remove","lines":["s"],"id":367}],[{"start":{"row":20,"column":31},"end":{"row":21,"column":0},"action":"insert","lines":["",""],"id":368},{"start":{"row":21,"column":0},"end":{"row":21,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":21,"column":8},"end":{"row":21,"column":9},"action":"insert","lines":["s"],"id":369}],[{"start":{"row":21,"column":9},"end":{"row":21,"column":10},"action":"insert","lines":["s"],"id":370}],[{"start":{"row":21,"column":9},"end":{"row":21,"column":10},"action":"remove","lines":["s"],"id":371}],[{"start":{"row":21,"column":8},"end":{"row":21,"column":9},"action":"remove","lines":["s"],"id":372}],[{"start":{"row":21,"column":8},"end":{"row":21,"column":9},"action":"insert","lines":["s"],"id":373}],[{"start":{"row":21,"column":9},"end":{"row":21,"column":10},"action":"insert","lines":["e"],"id":374}],[{"start":{"row":21,"column":10},"end":{"row":21,"column":11},"action":"insert","lines":["l"],"id":375}],[{"start":{"row":21,"column":11},"end":{"row":21,"column":12},"action":"insert","lines":["f"],"id":376}],[{"start":{"row":21,"column":12},"end":{"row":21,"column":13},"action":"insert","lines":["."],"id":377}],[{"start":{"row":21,"column":12},"end":{"row":21,"column":13},"action":"remove","lines":["."],"id":378}],[{"start":{"row":21,"column":11},"end":{"row":21,"column":12},"action":"remove","lines":["f"],"id":379}],[{"start":{"row":21,"column":10},"end":{"row":21,"column":11},"action":"remove","lines":["l"],"id":380}],[{"start":{"row":21,"column":9},"end":{"row":21,"column":10},"action":"remove","lines":["e"],"id":381}],[{"start":{"row":21,"column":8},"end":{"row":21,"column":9},"action":"remove","lines":["s"],"id":382}],[{"start":{"row":21,"column":8},"end":{"row":21,"column":9},"action":"insert","lines":["s"],"id":383}],[{"start":{"row":21,"column":9},"end":{"row":21,"column":10},"action":"insert","lines":["e"],"id":384}],[{"start":{"row":21,"column":10},"end":{"row":21,"column":11},"action":"insert","lines":["l"],"id":385}],[{"start":{"row":21,"column":11},"end":{"row":21,"column":12},"action":"insert","lines":["f"],"id":386}],[{"start":{"row":21,"column":12},"end":{"row":21,"column":13},"action":"insert","lines":["."],"id":387}],[{"start":{"row":21,"column":13},"end":{"row":21,"column":14},"action":"insert","lines":["c"],"id":388}],[{"start":{"row":21,"column":14},"end":{"row":21,"column":15},"action":"insert","lines":["l"],"id":389}],[{"start":{"row":21,"column":15},"end":{"row":21,"column":16},"action":"insert","lines":["i"],"id":390}],[{"start":{"row":21,"column":16},"end":{"row":21,"column":17},"action":"insert","lines":["e"],"id":391}],[{"start":{"row":21,"column":17},"end":{"row":21,"column":18},"action":"insert","lines":["n"],"id":392}],[{"start":{"row":21,"column":18},"end":{"row":21,"column":19},"action":"insert","lines":["t"],"id":393}],[{"start":{"row":21,"column":19},"end":{"row":21,"column":20},"action":"insert","lines":["s"],"id":394}],[{"start":{"row":21,"column":20},"end":{"row":21,"column":21},"action":"insert","lines":[" "],"id":395}],[{"start":{"row":21,"column":21},"end":{"row":21,"column":22},"action":"insert","lines":["+"],"id":396}],[{"start":{"row":21,"column":22},"end":{"row":21,"column":23},"action":"insert","lines":["="],"id":397}],[{"start":{"row":21,"column":23},"end":{"row":21,"column":24},"action":"insert","lines":[" "],"id":398}],[{"start":{"row":21,"column":24},"end":{"row":21,"column":25},"action":"insert","lines":["h"],"id":399}],[{"start":{"row":21,"column":25},"end":{"row":21,"column":26},"action":"insert","lines":["e"],"id":400}],[{"start":{"row":21,"column":26},"end":{"row":21,"column":27},"action":"insert","lines":["a"],"id":401}],[{"start":{"row":21,"column":27},"end":{"row":21,"column":28},"action":"insert","lines":["n"],"id":402}],[{"start":{"row":21,"column":28},"end":{"row":21,"column":29},"action":"insert","lines":["d"],"id":403}],[{"start":{"row":21,"column":29},"end":{"row":21,"column":30},"action":"insert","lines":["l"],"id":404}],[{"start":{"row":21,"column":29},"end":{"row":21,"column":30},"action":"remove","lines":["l"],"id":405}],[{"start":{"row":21,"column":28},"end":{"row":21,"column":29},"action":"remove","lines":["d"],"id":406}],[{"start":{"row":21,"column":27},"end":{"row":21,"column":28},"action":"remove","lines":["n"],"id":407}],[{"start":{"row":21,"column":26},"end":{"row":21,"column":27},"action":"remove","lines":["a"],"id":408}],[{"start":{"row":21,"column":26},"end":{"row":21,"column":27},"action":"insert","lines":["a"],"id":409}],[{"start":{"row":21,"column":26},"end":{"row":21,"column":27},"action":"remove","lines":["a"],"id":410}],[{"start":{"row":21,"column":25},"end":{"row":21,"column":26},"action":"remove","lines":["e"],"id":411}],[{"start":{"row":21,"column":25},"end":{"row":21,"column":26},"action":"insert","lines":["a"],"id":412}],[{"start":{"row":21,"column":26},"end":{"row":21,"column":27},"action":"insert","lines":["n"],"id":413}],[{"start":{"row":21,"column":27},"end":{"row":21,"column":28},"action":"insert","lines":["d"],"id":414}],[{"start":{"row":21,"column":28},"end":{"row":21,"column":29},"action":"insert","lines":["l"],"id":415}],[{"start":{"row":21,"column":29},"end":{"row":21,"column":30},"action":"insert","lines":["e"],"id":416}],[{"start":{"row":21,"column":30},"end":{"row":21,"column":31},"action":"insert","lines":["r"],"id":417}],[{"start":{"row":5,"column":23},"end":{"row":5,"column":24},"action":"remove","lines":["e"],"id":418}],[{"start":{"row":5,"column":22},"end":{"row":5,"column":23},"action":"remove","lines":["m"],"id":419}],[{"start":{"row":5,"column":21},"end":{"row":5,"column":22},"action":"remove","lines":["a"],"id":420}],[{"start":{"row":5,"column":20},"end":{"row":5,"column":21},"action":"remove","lines":["n"],"id":421}],[{"start":{"row":5,"column":20},"end":{"row":5,"column":21},"action":"insert","lines":["n"],"id":422}],[{"start":{"row":5,"column":21},"end":{"row":5,"column":22},"action":"insert","lines":["a"],"id":423}],[{"start":{"row":5,"column":22},"end":{"row":5,"column":23},"action":"insert","lines":["m"],"id":424}],[{"start":{"row":5,"column":23},"end":{"row":5,"column":24},"action":"insert","lines":["e"],"id":425}],[{"start":{"row":5,"column":23},"end":{"row":5,"column":24},"action":"remove","lines":["e"],"id":426}],[{"start":{"row":5,"column":22},"end":{"row":5,"column":23},"action":"remove","lines":["m"],"id":427}],[{"start":{"row":5,"column":21},"end":{"row":5,"column":22},"action":"remove","lines":["a"],"id":428}],[{"start":{"row":5,"column":20},"end":{"row":5,"column":21},"action":"remove","lines":["n"],"id":429}],[{"start":{"row":5,"column":20},"end":{"row":5,"column":21},"action":"insert","lines":["t"],"id":430}],[{"start":{"row":5,"column":21},"end":{"row":5,"column":22},"action":"insert","lines":["i"],"id":431}],[{"start":{"row":5,"column":22},"end":{"row":5,"column":23},"action":"insert","lines":["t"],"id":432}],[{"start":{"row":5,"column":23},"end":{"row":5,"column":24},"action":"insert","lines":["l"],"id":433}],[{"start":{"row":5,"column":24},"end":{"row":5,"column":25},"action":"insert","lines":["e"],"id":434}],[{"start":{"row":5,"column":16},"end":{"row":5,"column":17},"action":"remove","lines":["e"],"id":435}],[{"start":{"row":5,"column":15},"end":{"row":5,"column":16},"action":"remove","lines":["m"],"id":436}],[{"start":{"row":5,"column":14},"end":{"row":5,"column":15},"action":"remove","lines":["a"],"id":437}],[{"start":{"row":5,"column":13},"end":{"row":5,"column":14},"action":"remove","lines":["n"],"id":438}],[{"start":{"row":5,"column":13},"end":{"row":5,"column":14},"action":"insert","lines":["t"],"id":439}],[{"start":{"row":5,"column":14},"end":{"row":5,"column":15},"action":"insert","lines":["i"],"id":440}],[{"start":{"row":5,"column":15},"end":{"row":5,"column":16},"action":"insert","lines":["t"],"id":441}],[{"start":{"row":5,"column":16},"end":{"row":5,"column":17},"action":"insert","lines":["l"],"id":442}],[{"start":{"row":5,"column":17},"end":{"row":5,"column":18},"action":"insert","lines":["e"],"id":443}],[{"start":{"row":2,"column":11},"end":{"row":2,"column":12},"action":"remove","lines":["s"],"id":444}],[{"start":{"row":2,"column":10},"end":{"row":2,"column":11},"action":"remove","lines":["a"],"id":445}],[{"start":{"row":2,"column":9},"end":{"row":2,"column":10},"action":"remove","lines":["v"],"id":446}],[{"start":{"row":2,"column":8},"end":{"row":2,"column":9},"action":"remove","lines":["n"],"id":447}],[{"start":{"row":2,"column":8},"end":{"row":2,"column":9},"action":"insert","lines":["c"],"id":448}],[{"start":{"row":2,"column":9},"end":{"row":2,"column":10},"action":"insert","lines":["h"],"id":449}],[{"start":{"row":2,"column":10},"end":{"row":2,"column":11},"action":"insert","lines":["e"],"id":450}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":2,"column":11},"end":{"row":2,"column":11},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1520102121986}