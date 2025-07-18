def rem(l, word):
  n = []
  for items in l:
    if not(items == word):
      n.append(items.strip(word))
  return n 

l = ["masum", "shafi", "noman", "fi", "kafi", "nafi"]
print(rem(l, "fi"))