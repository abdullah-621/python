s = "abcde"

s = s[-1] + s[1:-1] + s[0]

print(s)

t = ''
for i in range(0, len(s)):
  if i % 2 == 0:
    t += s[i]
  else:
    continue

print(t)