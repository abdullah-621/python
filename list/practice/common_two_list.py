a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]

# a = set(a)
# b = set(b)

# c = list(a.intersection(b))

# print(c)
# print(type(c))

c = []

for i in a:
  if i in b:
    c.append(i)

  else:
    pass
print(c)