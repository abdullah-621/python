class Calculator:
    def __init__(self,fileName = "calculator.md"):
        self.fileName = fileName
    
    def save_file(self,x):
      with open(self.fileName,"a") as f:
        f.write(x)


    def expresion(self):
      expre = input("Enter your expresion : ")
      try:
        ans = eval(expre)
        print(f"\nAns : {expre } = {ans}")
        self.save_file(f"\n{expre} = {ans}\n")
      except ZeroDivisionError:
        print("\n⚠️ Anything can't divided by Zero.\n")
    

    def history(self):
      print("\n======= History ========\n")
      try:
        with open(self.fileName,"r") as f:
          contant = f.read()
          if contant.strip():
            print(contant)
          else:
             print("📂 No history found.\n")
      except FileNotFoundError:
         print("📂 History file not found.")

    def clear(self):
      with open(self.fileName,"w") as f:
        pass
      print("✅ History cleared!\n")
    

    def exit(self):
        print("👋 Exiting calculator...")



#  ========== Run ===========

calc = Calculator()
    

while True:
    print("")
    print("1. Expresion")
    print("2. History")
    print("3. Clear")
    print("4. Exit")
    print()

    try:
        # n = int(input("Enter number (1 - 4) : "))
        n = input("Enter number (expre,history,clear,exit) : ").strip().lower()
        if(n == "expre"):
            calc.expresion()
        elif(n == "history"):
            calc.history()
        elif(n == "clear"):
            calc.clear()
        elif(n == "exit"):
            calc.exit()
            break
        else:
            print("⚠️ Enter 1 to 4.")
            continue
    except ValueError:
        print("⚠️ Enter number 1 to 4.")

