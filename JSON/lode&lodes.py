"""
✅ lode = load from file
✅ dump = dump into file
✅ lodes = loads from string
✅ dumps = dumps into string
"""

import json

# load (from file)
with open("data.json", "r") as f:
    obj = json.load(f)
    print(obj)

# loads (from string)
json_str = '{"name": "Masum", "age": 24}'
obj2 = json.loads(json_str)
