a = {1,2,3,4,5}
b  = {4,5,6,7,8}
c = {6,7,8,9,10,11}

d = b.difference(a) # return a new set
# d = s - a or
print(d)

a.difference_update(b,c) # change the orginal set
# a -= b or
print(a)