import random

easy_passwords = [
    "1234",
    "password",
    "abcd",
    "qwerty",
    "admin",
    "letmein",
    "welcome",
    "user",
    "test",
    "love"
]
medium_passwords = [
    "sunshine123",
    "hello2025",
    "mypassword1",
    "blueSky99",
    "coffeeLover",
    "pythonRocks7",
    "summer2025",
    "happyDay88",
    "star12345",
    "flowerPower1"
]
hard_passwords = [
    "X9v$2k!bLq",
    "M@rbl3C@stle2025",
    "Tr0ub4dor&3",
    "QwErTy!2345",
    "F1sh!ngR0cks#99",
    "Zx!12aB#9kLm",
    "P@ssw0rd!$2025",
    "G@l@xy#77Moon",
    "C0mpL3x!ty#9",
    "R@1nB0w$Un1c0rn"
]


print("\n👋======= Welcome to Password Guess Game =======👋")

while True:
  level = input("\nEnter the level (easy, medium or hard) : ").lower()

  if(level == "easy"):
    password = random.choice(easy_passwords)
  
  elif(level == "medium"):
    password = random.choice(medium_passwords)
  
  elif(level == "hard"):
    password = random.choice(hard_passwords)
  
  else:
    print("\nChose the right level.")
    password = random.choice(easy_passwords)

  no_of_attempt = 0

  your_guess = ["_"]  * len(password)


  len_of_password = len(password)


  while "".join(your_guess) != password:

    print("\nLevel : ",level)
    print("Password length : ",len_of_password)
    print("Your progress : "," ".join(your_guess))
    ans = input("Enter your guess : ")

    if len_of_password != len(ans):
      print("\n ⚠️ Write the right length of your guess.\n")
    
    else:
      # print("Your need to fill up : ",your_guess)

      for i in range(len(password)):
        if ans[i] == password[i]:
          your_guess[i] = ans[i]
        else:
          pass
      no_of_attempt += 1

  
  print("\nYour attempt time : ",no_of_attempt)
  print("🎉 Congratulation! 🎉\n")

  again = input("Do you went to play again (Yes/No) :").lower()
  if again == "yes":
      continue
  else:
      print("Good Bye......")
      break
      

