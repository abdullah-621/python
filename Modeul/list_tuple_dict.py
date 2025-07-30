l = [("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]

t = dict()

for x,y in l:
  t.setdefault(x,[]).append(y)

print(t)