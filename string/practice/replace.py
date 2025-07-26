# def replaceChar(str, char):
  
#   result = ''

#   for i in range(0,len(str)):

#     if str[i] == char and i != 0:
#       result += '$'

#     else:
#       result += str[i]
  
#   return result

# print(replaceChar("masum mama",'m'))

def replaceChar(str):
  
 char = str[0]

 str = str.replace(char,'$')

 str = char + str[1:]

 return str

print(replaceChar("masum mama"))