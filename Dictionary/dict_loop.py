nums = {
  "rohan" : 23,
  "masum" : "abdullah",
  "fruits" : ["mango","banana","potato"],
  "rohan" : 25
}

# print keys
for i in nums:
  print(i)

# print values
for i in nums:
  print(nums[i])

# print keys
for i in nums.keys():
  print(i)

# print values
for i in nums.values():
  print(i)

# print key , value pairs
for i,j in nums.items():
  print(i , " : " ,j)