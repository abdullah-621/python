def makeGreat(s):
  if len(s) == 0:
    return s
  
  stack = []

  for char in s:
    if not stack or abs(ord(stack[-1])  - ord(char)) != 32:
      stack.append(char)

    else:
      stack.pop()

  return ("".join((stack)))


s = "LeEeetcode"
print(makeGreat(s))


