"""
✅ lode = load from file
✅ dump = dump into file
✅ lodes = loads from string
✅ dumps = dumps into string
"""

import json

data = {"name": "Abdullah AL Noman", "age": 24}

# dump (to file)
with open("data.json", "w") as f:
    json.dump(data, f)


# # dumps (to string)
# json_string = json.dumps(data)
# print(json_string)  
# Output: {"name": "Masum", "age": 24}
