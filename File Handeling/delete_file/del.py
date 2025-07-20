import os

# os.remove("rem.txt") # if exists

if os.path.exists("rem.txt"):
  os.remove("rem.txt")
else:
  print("This file does not exist.")

# os.rmdir("oi") # if exists
# rmdir only delete empty folders

if os.path.exists("oi"):
  os.rmdir("oi")
else:
  print("This folder does not exist.")
