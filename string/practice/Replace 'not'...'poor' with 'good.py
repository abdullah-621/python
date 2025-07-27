def replace(str):
  

  find_not = str.find('not')
  find_poor = str.find('poor')

  # ans = ""
  if (find_not < find_poor) and find_not > 0 and find_poor > 0:
    # ans += str[0:find_not]
    # ans += "good"
    str = str.replace(str[find_not:(find_poor + 4)],'good')
    return str;
  else:
    return str;

String = 'The lyrics is not that poor in enclusive!'

print(replace(String))