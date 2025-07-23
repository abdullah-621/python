nums = [1,2,3,4,5,6]

i = 0
j = len(nums) - 1

while (i < j):
  n = nums[i]
  nums[i] = nums[j]
  nums[j] = n
  i += 1
  j -= 1

print(nums)