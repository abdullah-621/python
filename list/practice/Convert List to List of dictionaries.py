a = ["name", "age", "city"]

b = [["Alice", 25, "New York"], ["Bob", 30, "Los Angeles"], ["Charlie", 22, "Chicago"]]

res = []

for value in b:
  print(value)
  d = {a[i]: value[i] for i in range(len(a))}
  res.append(d)


print(res)