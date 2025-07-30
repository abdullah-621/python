from itertools import product

my_dict = {'1':['a','b'], '2':['c','d']}

a = list(my_dict.values())

for x,y in product(a[0], a[1]):
  print(x + y)



