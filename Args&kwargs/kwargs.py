# **kwargs is a keyWord agruments

def display_info(**kwargs): # **kwargs basically a dict
  print(type(kwargs))
  for key,value in kwargs.items():
    print(key, "=>", value)

display_info(name = "Abdullah Al Masum", age = 35, home = "JP",product="Laptop", price=1200)