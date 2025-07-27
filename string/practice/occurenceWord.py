def OccurenceWord(str):
  List = str.split(' ')

  # my_dict = {}

  # for word in List:
  #   if word in my_dict:
  #     my_dict[word] += 1

  #   else:
  #     my_dict[word] = 1

  my_dict = {word : List.count(word) for word in List}  # dict comprehension

  return my_dict


s = "Write a Python program to count the occurrences of each word in a given sentence."

d = OccurenceWord(s)

print(d)