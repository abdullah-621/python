nums = [5,4,3,2,1]
nums.sort()  # sort orginal list
print(nums)

a = [5,4,3,2,1]
b = sorted(a) # this function will return a sorted list
print(a)


def my_fun(n):
  return abs(n - 50)

thisList = [100,50,23,82,65]
thisList.sort(key = my_fun)
print(thisList)