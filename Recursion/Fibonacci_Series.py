
# n = int(input("Enter the number : "))

# a = 0
# b = 1

# if n == 0: print(0)
# elif n == 1: print(1)
# else:
#   for i in range(2 ,n + 1):
#     next = a + b
#     a = b
#     b = next
#     print(next, end = " ")


# todo : using recursion

def Fibonacci_Series(n):
  if n == 0 : return 0
  if n == 1 : return 1

  return Fibonacci_Series(n - 1) + Fibonacci_Series(n - 2)


n = int(input("Enter the number : "))

print(Fibonacci_Series(n))