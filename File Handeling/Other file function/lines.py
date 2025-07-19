f = open("o.txt")
lines = f.readlines()  # return a list

print(lines)
print(type(lines))

f.close()


# line = f.readline()  # retunr a first (single) line
# print(line)
# print(type(line))

# while(line != ""):
#   print(line)
#   line = f.read()
