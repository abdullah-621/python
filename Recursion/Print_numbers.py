def print_number(n):
  if n == 0 :
    return
  print_number(n - 1)
  print(n , end=" ")


n = int(input("Enter the number : "))
print_number(n)