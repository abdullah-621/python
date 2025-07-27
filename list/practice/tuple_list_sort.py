def last(n):
  print(n)
  return n[-1]

def sort_tuple_list(tuples):
  
  return sorted(tuples, key = last)



tuples = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
SL = sort_tuple_list(tuples)
print(SL)