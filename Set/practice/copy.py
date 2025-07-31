from copy import deepcopy
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

s3 = s1.copy()
s3.add(3456)

print(s3)