a = ['gfg', 'is', 'best', 'for', 'geeks']

# List of characters to check for
remove_chars = ['g', 'e']

# ans = [word for word in a if not any(char in word for char in remove_chars)]

ans = []

for word in a:
  if not any(char in word for char in remove_chars):
    ans.append(word)


print(ans)