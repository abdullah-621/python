import os
with open("log.txt") as f:
  content = f.read()

# os.makedirs("copy" , exist_ok = True) # when folder not exist

with open("copy/copy_log.txt" , "w") as c:
  c.write(content)