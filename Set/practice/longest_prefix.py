# def longest_prefix(strs):
#   if not strs:
#     return ""

#   min_len = min([len(word) for word in strs])


#   for i in range(min_len):

#     chars = set([words[i] for words in strs])

#     if len(chars)> 1:
#       return strs[0][:i]
    
#   return strs[0][:min_len]



# strs = ["w3re", "w3resource"]
# print(longest_prefix(strs))

a = {1, 2, 3, 4, 5, 6}
b = {3, 4, 5, 6, 7, 8}


print("missing in b : ",a.difference(b))
print("missing in a : ",b.difference(a))