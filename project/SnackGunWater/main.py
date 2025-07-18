# 1 => snack
# -1 => water
# 0 => gun
"""
  Gesture	     Beats

🔫 Gun	(0)      beats Snack
🍿 Snack(1)	     beats Water
💧 Water(-1)	   beats Gun
"""
import random

print("🎮 Welcome to Water-Snack-Gun Game!")
print("🔫 (g)un beats 🍿 (s)nack")
print("🍿 (s)nack beats 💧 (w)ater")
print("💧 (w)ater beats 🔫 (g)un\n")

r = int(input("Enter number of rounds : "))
print()

you_win = 0
you_lose = 0
match_draw = 0

for i in range(r):

  
  you_input = input("Enter you input : ")

  if(you_input == 's' or you_input == 'g' or you_input == 'w'):
     
    print()
    computer = random.choice([-1, 0 , 1])
    you_dict = {"s" : 1, "w" : -1, "g" : 0}
    reverse_dict = {1 : "🐍 snack" , -1 : "💧 water" , 0 : "🔫 gun"}

    you = you_dict[you_input]

    print(f"you chose {reverse_dict[you]} \ncomputer chose {reverse_dict[computer]}")

    if(you == computer):
      print("Match Draw")
      match_draw += 1
      print()

    # else:
    #   if(you == 1 and computer == -1):
    #     print("You win!")

    #   elif(you == -1 and computer == 0):
    #     print("You win!")

    #   elif(you == 0 and computer == 1):
    #     print("You win!")

    elif (you == 1 and computer == -1) or (you == -1 and computer == 0) or (you == 0 and computer == 1) :
      print("You win!")
      you_win += 1
      print()


    else:
        print("You lose!")
        you_lose += 1
        print()
  else:
     print("Please enter a valid input (g , s or w)")
     r += 1
   
print()

if(you_win == 0):
   print(f"You win : {you_win} 😞")

else:
   print(f"You win : {you_win} ☺️")

if(you_lose == 0):
   print(f"You lose : {you_lose} 😅")

else:
   print(f"You lose : {you_lose} 😕")

print(f"Match draw : {match_draw} 🥹")
                                  
# print(f"You win : {you_win}\nYou lose : {you_lose}\nMatch draw : {match_draw}")
print()