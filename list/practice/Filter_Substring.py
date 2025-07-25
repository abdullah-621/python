test_list1 = ["Gfg", "is", "not", "best", "and", "not", "CS"]

test_list2 = ["Its ok", "all ok", "wrong", "looks ok", "ok", "wrong", "thats ok"]

sub_str = "ok" 

# ans = []
# for i in range(len(test_list2)):
#   if sub_str in test_list2[i]:
#     ans.append(test_list1[i])

# ans = [test_list1[word] for word in range(len(test_list2)) if sub_str in test_list2[word]]

ans = []

for i in range(len(test_list2)):
  if test_list2[i].find(sub_str) != -1:
    ans.append(test_list1[i])
  else:
    pass


print(ans) 
