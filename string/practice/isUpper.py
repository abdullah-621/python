def convertUpper(str):
  print(id(str))
  count_up = 0

  for i in range(0, 4):
    if str[i].isupper():
      count_up += 1

  if count_up >= 2:
    str = str.upper()
    print(id(str))

  return str

s = 'PyThon\n'

a = convertUpper(s)
print(a)

s = sorted(a,reverse=True)
print(''.join(s))


d = {'mas': 1, "nums":2}
print(''.join(d.keys()))
