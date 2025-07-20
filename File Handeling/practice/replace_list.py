
words = ["donkey", "bad", "very"]

with open("replace.txt", "r") as f:
  contant = f.read()

# newContant = contant

for i in words:
 if (i == "donkey"):
  contant = contant.replace(i, "#" * len(i))
 elif (i == "bad"):
  contant = contant.replace(i, "*" * len(i))
 else:
  contant = contant.replace(i, "@" * len(i))

with open("replace.txt", "w") as f:
  f.write(contant)