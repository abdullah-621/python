class cla1:
  a = 1

class cla2(cla1):
  b = 2

class cla3(cla2):
  c = 3

o = cla1()
o = cla2()
o = cla3()

print(o.a)
print(o.b,o.b)
print(o.a,o.b,o.c)