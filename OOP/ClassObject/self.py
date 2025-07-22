class masum:  

  first_name = "Abdullah"  
  last_name = "Masum"
  age = 22
  home = "joypurhat"

  def getInfo(self):
    print(f"His name is : {self.first_name} \nHis home is : {self.home}")

  @staticmethod
  def greet():
    print("Static method when no need any self attribute")




z = masum()  
z.getInfo()
z.greet()
# masum.getInfo(z)


