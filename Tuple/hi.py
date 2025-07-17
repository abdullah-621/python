fruits = ("mango","orange","banana","jackfruit","painaple","mango")
fruits = tuple(("mango","orange","banana","jackfruit","painaple","mango"))

print(type(fruits))
print(fruits)

nums = ["shafi","kalam","rakib","nipu"]

x = tuple(nums)
print(type(x))

fruit = input("Enter the fruit name : ")
if fruit in fruits:
  print(f"Yes! {fruit} is here")
else:
  print(f"No! {fruit} is not here")


