def natural_sum(n):
  if n == 0 : return 0
  if n == 1 : return 1

  return n + natural_sum(n - 1)

n = int(input("Enter the number : "))
print(f"sum of {n} natural is : {natural_sum(n)}")
