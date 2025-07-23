nums = [1,2,3,4,5,6,7,8,9,10]

even = [val for val in nums if val % 2 == 0]
odd = [val for val in nums if val % 2 != 0]

print(even, odd)