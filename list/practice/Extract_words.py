test_list = ["geekforgeeks", "is", "best", "for", "geeks"]

k  = 'g'
ans = [word for word in test_list if word.startswith(k)]

# for word in test_list:
#   if word.endswith(k):
#     ans.append(word)


print(ans)