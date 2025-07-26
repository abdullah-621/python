import random

number = random.randint(1,20)

# print(number)

l = []
num = -1
# times = 0

while (num != number):
  num = int(input("Guess the number : "))
  l.append(num)
  # times += 1

  if(num > number):
    print(f"{num} is gratter then number.")
  
  else:
     print(f"{num} is lower then number")
     

print(f"\n\n{l}\nCongratulation !!!\nyou are right.\nYou types : {len(l)} times\n\n")