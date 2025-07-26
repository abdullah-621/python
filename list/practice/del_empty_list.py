l = [[1,2,3],[],[2,3,4],[]]

e = []

for i in l:
  if i:      # pyhton treats this [] as false.
    e.append(i)

print(e)
