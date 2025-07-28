a = [1,2,3,4,5,6,[2,3]]
b = [2,3]

flag = True

for i in b:
  if i not in a:
    flag = False
    break
  else:
    pass

if flag:
  print("yes SubList")
else:
  print("Not Sublist")