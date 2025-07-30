a = {1:2, 4:5}
b = {6:7, 8:9}
c = {2:4, 9:0}

d = {}

for i in (a,b,c):
  d.update(i)

print(d)