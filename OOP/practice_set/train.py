from random import randint
class train:

  def __init__(self, trainNo):
    self.trainNo = trainNo

  def book(self, fro, to):
    print(f"Ticket is booked in train no : {self.trainNo} from {fro} to {to}")

  def getStatus(self):
    print(f"Your train TC {self.trainNo} is running on time")

  def getFair(self, fro, to):
    print(f"ticket fair is train no {self.trainNo} from {fro} to {to} in {randint(355, 899)}")


t = train(123)
t.book("joypurhat", "dhaka")
t.getStatus()
t.getFair("joypurhat", "dhaka")