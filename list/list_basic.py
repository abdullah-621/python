num = ["apple","mango",23,45.6,False]
# print(num[3:5])

item = input("Enter the items : ")

if item.lower() == "false":
  item = False
elif item.lower() == "true":
  item = True

if item in num:
  print(f"Yes {item} is present this list.")
else:
  print(f"No {item} is not present this list.")


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon","kew"]
print(thislist)

thislist.insert(3,"hello");
print(thislist)
thislist.clear()
print(thislist)