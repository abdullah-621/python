d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0, 6: 5}

idx = lambda item : item[1]

x = dict(sorted(d.items(), key = idx))

print(x)

# items = d.items()

# for item in items:
#   print(item)



