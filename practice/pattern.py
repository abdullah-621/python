row = int(input("Enter row : "))

for i in range(1 , row + 1):
  if i == 1 or i == row:
   print("*" * row)

  else:
    print("*", end="")
    print(" " * (row - 2), end="")
    print("*")


  

