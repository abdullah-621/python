with open("append.txt", "a") as f:
  f.write("Appned this line after this content")

r = open("append.txt")
print(r.read())
r.close()