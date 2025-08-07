def file_read(name):
  read = open(name)
  print(read.read())
  read.close()

file_read("txt.md")