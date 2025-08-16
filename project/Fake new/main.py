import random

subject = [
  "Masum",
  "Shafi",
  "Noman",
  "Akash",
  "Nipu",
  "Rakib",
  "A group of monkeys",
]

action = [
  "launches",
  "cancels",
  "dance with",
  "eats",
  "declares war on",
  "celebration",
]

palce_or_thinks = [
  "at Red Fort",
  "in Mumbai local train",
  "a plate of somasa",
  "during study",
  "at india gate",
]

o = open("funny.txt","w")
w = o.write("==============> BREAKING NEWS <=============== \n")
o.close()

while True:
  try:
    again = int(input("Do you want to genarate fake news.\nIf yes press(1) otherwise (0) :"))

    if again == 0:
      break
    else:
      if again < 0 or again > 1:
        print("Please enter 0 or 1\n")
        continue
        
  except ValueError:
    print("Enter the number (0 or 1).\n")
    continue

  sub = random.choice(subject)
  act = random.choice(action)
  place = random.choice(palce_or_thinks)

  jokes = f"\n{sub} {act} {place}.🤣\n"
  print(jokes)

  with open("funny.txt",'a',encoding="utf-8") as f:
    f.write(jokes)

  

