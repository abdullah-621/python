def swapChar(s,t):

  a = t[:2] + s[2:]
  b = s[:2] + t[2:]
  
  return (f"{a} {b}")

print(swapChar("masum","noman"))