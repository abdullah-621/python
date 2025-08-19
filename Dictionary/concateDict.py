dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60, 1:90}

# Method 1
dic4 = dic1 | dic2 | dic3
print(dic4)

# Method 2
dic1.update(dic2)
dic1.update(dic3)
print(dic1)

# Method 3
merged = {**dic1, **dic2, **dic3}
print(merged)