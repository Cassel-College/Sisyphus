import json

class JsonBox:
    
    def __init__(self, json_string):
        self.json_data = json.loads(json_string)

    def get_value(self, key):
        return self.json_data[key]

    def set_value(self, key, value):
        self.json_data[key] = value

    def to_string(self):
        return json.dumps(self.json_data)
