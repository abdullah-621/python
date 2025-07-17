set1 = {1,2,3,4}
set2 = {2,4,5,6}


# Can not modifies original set return new set
# union() join all the unique values form Eatch sets

print(set1.union(set2)) 
print(set1 | set2) # | can not join another type like tuple,


# print(set1.update(set2)) # print none because modifies original set can not return new set
# set1.update(set2)
# print(set1)

print(set1.intersection(set2))
print(set1 & set2)


print(set2.difference(set1))
print(set2.symmetric_difference(set1))