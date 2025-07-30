l1 = ['one','two','three']
l2 = [1,2,3]
# my_dict = {}

# for i in range(len(l1)):
#   my_dict[l1[i]] = l2[i]

# print(my_dict)

my_dict = dict(zip(l1,l2))
print(my_dict)
