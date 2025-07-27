def long_word(n, str):
  ans = []
  l = str.split()

  for word in l:
    if len(word) > n:
      ans.append(word)

    else:
      pass

  return ans

print(long_word(3, "The quick brown fox jumps over the lazy dog"))