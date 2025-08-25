# *args this is a positional argument

def add(*args):  # this args basically a tuple
  print(type(args))
  print(sum(args))


add(1,2,3,4,5)