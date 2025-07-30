a = {1,2,3,4,5,6,7,8}
b  = {6,7,8}

super = a.issuperset(b)
# super = a >= b
# super = a > b
print(super)
sub = b.issubset(a)
print(sub)
