nums = [123, 445, 779]

ans = []

for i in nums:
  total = 0
  val = i

  while (val != 0):
    total += (val % 10)
    val /= 10

  ans.append(total)
  total = 0

print(ans)