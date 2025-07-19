
# f = open("poems.txt")
# r = f.read()

# if ("Twinkle" in r):
#   print("Yes, Twinkle is here!")
# else:
#   print("Twinkle is not present")

# f.close()

with open("poems.txt") as o:
  contant = o.read()
  if ("Twinkle" in contant):
   print("Yes, Twinkle is here!")
  else:
   print("Twinkle is not present")