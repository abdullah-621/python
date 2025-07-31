s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

s3 = s2.intersection(s1)
s4 = s1.union(s2)
s5 = s1.difference(s2)
s6 = s1.symmetric_difference(s2)
print("intersection : ",s3)
print("union : ",s4)
print("difference : ",s5)
print("symmetric : ",s6)
print(s2.issubset(s1))