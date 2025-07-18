def gratest(x , y, z):
  if x > y and x > z :
     return ("x is greatest");
  elif y > x and y > z :
    return ("y is greatest");
  else:
    return ("z is greatest");

x = int(input("Enter x :"))
y = int(input("Enter y :"))
z = int(input("Enter z :"))

grat = gratest(x, y, z)
print(grat)