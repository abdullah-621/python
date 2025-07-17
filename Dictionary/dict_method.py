nums = {
  "rohan" : 23,
  "masum" : "abdullah",
  "fruits" : ["mango","banana","potato"],
  "rohan" : 25
}

print(nums["masum"])
print(nums.get("masum2"))  # if not exist return nono

# get keys
x = nums.keys()
print(x)
nums["shafi"] = 23
print(x)

# get values
y = nums.values()
print(y)
nums["shafi"] = 25
print(y)

# get items
z = nums.items()
print(z)
nums["noman"] = 18
print(z)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "manufacture" : "nike"
}

newdict = thisdict.copy()
print(newdict)

# Removing Items
thisdict.pop("model")
print(thisdict)
# thisdict.popitem()
del thisdict["year"]
print(thisdict)
thisdict.clear()
print(thisdict)
del thisdict # delete all the dict
# print(thisdict)

nums.update({"kire" : 98})

print(nums)