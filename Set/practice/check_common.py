s1 = {1,2,3,8}
s2 = {4,5,6,7,8}

s3 = s1.intersection(s2)

if len(s3) == 0:
  print("No Common")
else:
  print("Common :",s3)