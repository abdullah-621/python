tuplex = "w", 3, "r", "s", "o", "u", "r", "c", "e"

idx = tuplex.index('s')

tuplex = tuplex[:idx] + tuplex[idx + 1:]

print(tuplex)
print(len(tuplex))

d = dict(list(tuplex))
print(d)