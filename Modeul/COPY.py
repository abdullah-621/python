import copy
'''
shallow copy will not change orginal list either the list is one dimension it only change when the list are multiple dimenton and it just change those dimensional object.

But DeepCopy will not change any type of list either one or more dimension.
'''
l = [1, [2, 3, 4]]
a = copy.deepcopy(l)
a[1][0] = 19
l.append([89,90,90])

print("l =", l)
print("a =", a)

# t = (1,2,3,4,[2,3,4])
# a = deepcopy(t)
# a[4][2] = 1000
# print(t)
# print(a)
