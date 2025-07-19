f = open("o.txt")
r = f.read()
print(r)
f.close()


with open("o.txt") as f:  # No need to close the file
  print(f.read())