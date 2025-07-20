
with open("log.txt") as f:
  contant = f.read()

  if ("python" in contant):
    print("Yes! present")
  else:
    print("Not present")