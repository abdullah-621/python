def outer():
  a = 5
  def inner():
    print(a)
  
  return inner

b = outer()
b()