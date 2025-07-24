test_list = ["geeksforgeeks", "best", "geeks", "and", "geeks", "love", "CS"]

res = 'geek'

ans = []


for val in test_list:

  if val.startswith(res):
    ans.append([val])

  else:
    ans[-1].append(val)

print(ans)
  