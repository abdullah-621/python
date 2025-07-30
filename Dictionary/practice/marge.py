d1 = {'a': 10, 'b': 20}

d2 = {'x': 30, 'y': 20}

d = d1.copy()
d.update(d2)


d_sum = sum(d.values())


d_mul = 1

for i in d.values():
  d_mul = d_mul * i;

print(d_mul)
print(d_sum)
print(d)