def count_word_freq(words):
  words_set = set(words)

  d = dict()

  for i in words_set:
    n = words.count(i)
    d.update({i : n})

  return d



words = ['Red', 'Green', 'Red', 'Blue', 'Red', 'Red', 'Green']
print(count_word_freq(words))