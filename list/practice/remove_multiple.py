nums = [1,2,3,4,5,6,7,8,9,10]

remove = [2,5,9]

n = [val for val in nums if val not in remove]

print(n)