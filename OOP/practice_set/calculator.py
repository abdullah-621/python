import math

class Calculator:
  def __init__(self, n):
    self.n = n
  
  def squre(self):
    print(f"Squre is : {self.n * self.n}")
  
  def qube(self):
    print(f"Qube is : {self.n * self.n * self.n}")

  def root(self):
    print(f"Root is : {math.sqrt(self.n)}")


c = Calculator(9)
c.squre()
c.qube()
c.root()