"""
There are three types of number
# int
# float
# complex

"""

a = 3
b = 4.5
c = 5j # We cannot convert complex numbers into another number type.

print(type(a), " : " , a)
print(type(b), " : " , b)
print(type(c), " : " , c)

a = float(a);
b = int(b);
c = complex(b)

print(type(a), " : " , a)
print(type(b), " : " , b)
print(type(c), " : " , c)
