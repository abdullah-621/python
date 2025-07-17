fruits = ("mango","orange","banana","jackfruit","painaple","mango")

change_into_list = list(fruits)

change_into_list[1] = "potato"

fruits = tuple(change_into_list);

print(fruits)

y = ("potato","strawberry")

new_tuple = fruits + y 

print(new_tuple)
print(type(new_tuple))

i = 0

while(i < len(fruits)):
  print(fruits[i])
  i += 1

  