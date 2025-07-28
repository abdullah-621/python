my_list = [10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30]

my_dict = {}

for i in my_list:
  if i in my_dict:
    my_dict[i] += 1

  else:
    my_dict[i] = 1

print(my_dict)