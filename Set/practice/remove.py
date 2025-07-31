s1 = {1,2,30,4,0,5}
# s2 = {4,5,6,7,8}
print(30 in s1)
print(len(s1))
l = list(s1)
l.sort()
print(f"Min value : {l[0]}\nMax value : {l[len(l) - 1]}")

s1.clear()

print(s1)