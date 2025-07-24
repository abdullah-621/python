test_list = ["geekforgeeks", "is", "best", "for", "geeks"]
k = 21
str = "".join(test_list)

idx = str[k]
k = -1

for val in test_list:
  if idx in val:
    for i in range(len(val)):
      if val[i] == idx:
        k = i
        break
  break

print(k)
