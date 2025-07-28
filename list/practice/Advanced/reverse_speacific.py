def reverse(nums,start_pos, end_pos):
  
  while(start_pos < end_pos):
    temp = nums[start_pos]
    nums[start_pos] = nums[end_pos]
    nums[end_pos] = temp
    start_pos += 1
    end -= 1

  return nums


nums = [1,2,3,4,5,6,7,8,9,10]
reverse(nums,3,7)
print(nums)