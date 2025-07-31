def find_pair(nums,target):

  nums = set(nums)

  pairs = []

  for n in nums:
    complement = target - n
    if complement in nums:
      pairs.append({n,complement})
  return pairs


nums = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,20]
print("Original list of numbers:")
print(nums)
target_val = 35
print(find_pair(nums, target_val))