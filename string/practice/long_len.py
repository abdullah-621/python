def long_len(l):
  
  length = 0

  for word in l:
    if(len(word) > length):
      length = len(word)
    
    else:
      pass
  return length

l = ['abdullah','al','masum']
print(long_len(l))