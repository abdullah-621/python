
word = "donkey"

with open("replace.txt", "r") as f:
  contant = f.read()

newContant = contant.replace(word, "####")

with open("replace.txt", "w") as f:
  f.write(newContant)