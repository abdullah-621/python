nums = [10,20,10,30,40,50,20,80,3,9]

dup_items = set()
uni_items = []

for i in nums:
  if i not in dup_items:
    uni_items.append(i)
    dup_items.add(i)

  else:
    pass

print(dup_items)
print(uni_items)

# uni_items = set(nums)
# uni_items = list(uni_items)
# print(uni_items)
