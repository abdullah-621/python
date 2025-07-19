import random

def game_score():
 n = random.randint(10, 30)
 return n

# print(score())

score = game_score()
print(f"Your score is : {score}")

with open("game.txt", "r") as contant:
 high_score = contant.read()
 if high_score != "":
  high_score = int(high_score)
 else:
  high_score = 0
if (high_score < score):
 with open("game.txt", "w") as contant:

  print("Your score is higher then the high_score. Updated")
  contant.write(str(score))

else:
    print("Your score is less then the high score")