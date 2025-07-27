def long_len(l,idx):

  # s = ''

  # for i in range(0,len(l)):
  #   if i != idx:
  #     s += l[i]

  #   else:
  #     continue
  first_part = l[ : idx]
  last_part = l[idx+1 : ]

  return first_part + last_part
  
  

l = 'abdullah'
print(long_len(l,4))