fruits = {"mango","orange","banana","jackfruit","painaple","mango"}

for x in fruits:
  print(x)

if("mango" in fruits):
  print("yes it's here")

# add items (but can't cahange the sets)
fruits.add("potato")
print(fruits)

# Add sets
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

# Add elements of a list to at set
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

# remove items
thisset.remove("apple")

thisset.discard("banana")

x = thisset.pop() # del a rendom items
print(x)
print(thisset)

thisset.clear()
print(thisset)
del thisset
print(thisset)


