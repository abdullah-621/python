def check_anagram(strs):

  result = {}

  for word in strs:

    sorted_word = "".join(sorted(word))
    # print(sorted_word)

    if sorted_word in result:
      result[sorted_word].append(word)

    else:
      result[sorted_word] = [word]

  return result



strs = ['eat', 'cba', 'tae', 'abc', 'xyz']
print(strs)
print(check_anagram(strs))
