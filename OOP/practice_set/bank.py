class Bank:
  def __init__(self):
    self.customers = {}

  def create_account(self,account_number,initial_balance = 0):
    if account_number in self.customers:
      print("Account number already exists.")
    else:
      self.customers[account_number] = initial_balance
      print("Account created successfully")
    
  def make_deposite(self,account_number,amount):
    if account_number in self.customers:
      self.customers[account_number] += amount
      print("deposite successfully")
      print("Account balance :",self.customers[account_number])

    else:
      print("Account number dose not exist.Please check again.\nYou have no account.\nDo you want to creat an account.\nif yes then enter 1 otherwise 2.")

      try:
          n = int(input("Enter 1 (yes) or 2 (No):"))
      except ValueError:
        print("Invalid input.please enter number.")
        return
      
      if n == 1:
        self.create_account(account_number,amount)
        print("Now you can deposite.")
      else:
        return
  
  def make_withdraw(self,account_number,amount):
    if account_number in self.customers:
      amnt = self.customers[account_number]
      if amount <= amnt:
        self.customers[account_number] -= amount
        print("Withdraw successfully.")
        print("Account balance :",self.customers[account_number])
      else:
        print("Your amount out of the range.please enter legal amount")
    else:
      print("Account number does not exist.Please check again.")

  def check_balance(self,account_number):
    if account_number in self.customers:
      print("Account balance :",self.customers[account_number])
    else:
      print("Account number does not exist.Please check again.")

  def del_account(self,account_number):

    if account_number in self.customers:
      print("Are you sure to delete your account.\nIf yes enter 1 or No enter 2.")

      try:
          n = int(input("Enter 1 (yes) or 2 (No):"))
      except ValueError:
        print("Invalid input.please enter number.")
        return

      if n == 1:
        del_ac = self.customers.pop(account_number)
        print(f"Account {account_number} deleted successfully.")
        return del_ac
      else:
        print("Okey, What's your mind.")
    else:
      print("Account number deos not exist")


bank = Bank()
bank.create_account(2023200000621,2000000)
bank.check_balance(2023200000621)
bank.make_deposite(2023200000622,300000)
bank.make_withdraw(2023200000621,2000)
print(bank.customers)
bank.del_account(2023200000623)
print(bank.customers)
