# a = ['2', '4', '6', '8']

# b = [int(i) for i in a]

# # for i in a:
# #   b.append(int(i))

# print(b)


s = 'Geeks, for, Geeks'

# a = s.split(',')
a = []

for item in s.split(','):
    print(item)
    a.append(item.strip())
print(a)