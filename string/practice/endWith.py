def endWith(str):
  
  if len(str) >= 3 and not str.endswith("ing"):
    str = str + "ing"

  elif(len(str) >= 3 and str.endswith("ing")):
    str = str + 'ly'

  else:
    pass
  
  return str

print(endWith("ac"))        # abc
print(endWith("play"))       # playing
print(endWith("playing")) 
