def countFreq(str):

  dict = {}

  for i in str:
    keys = dict.keys()

    if i in keys:
      dict[i] += 1
    
    else:
      dict[i] = 1
      
  return dict


str = input("Enter your string : ")
r = countFreq(str)
print(r)


