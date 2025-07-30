a = {1,2,3,4,5}
b  = {4,5,6,7,8}

c = a.intersection(b)
# c = a & b
print(c)

# a.intersection_update(b)
a &= b
print(a)