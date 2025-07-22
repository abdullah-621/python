class cla1:

  def __init__(self):
    print("Cla1 constractor")
  a = 1

class cla2(cla1):
  def __init__(self):
    super().__init__()
    print("Cla2 constractor")
  b = 2

class cla3(cla2):
  def __init__(self):
    super().__init__()
    print("Cla3 constractor")
  c = 3

o1 = cla1()
o2 = cla2()
o3 = cla3()

print(o1.a)
print(o2.a,o2.b)
print(o3.a,o3.b,o3.c)