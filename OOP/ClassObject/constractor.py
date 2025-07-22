class masum:  

  first_name = "Abdullah"  
  last_name = "Masum"
  age = 22
  home = "joypurhat"

  def __init__(self, first_name, age, home):
    self.first_name = first_name
    self.age = age
    self.home = home
    print("Hey I am init method.")
    

  def getInfo(self):
    print(f"His name is : {self.first_name} \nHis home is : {self.home}")

  @staticmethod
  def greet():
    print("Static method when no need any self attribute")


z = masum("Noman", "16", "Dhaka")  
z.getInfo()
z.greet()
# masum.getInfo(z)


