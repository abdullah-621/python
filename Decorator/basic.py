"""
Decorator is a function which need a function and then add some functionality and return it
"""


# def my_decorator(func):
#   def wrapper():
#     print("********************")
#     func()
#     print("********************")
  
#   return wrapper

# @my_decorator
# def hello():
#   print("Hello World !")

# hello()

# # a = my_decorator(hello)
# # a()

def display(*agrs):
  print(agrs)
  print(sum(agrs))

display(1,2,3,4,5)