class animals:
  def __init__(self,color,legs):
    self.color = color
    self.legs = legs
  
  def showAnimal(self):
    print("This is a animal class")


class pets(animals):
  def __init__(self,color,legs,wenks):
    super().__init__(color,legs)
    self.wenks = wenks
  
  def showpets(self):
    print(f"pets have {self.wenks} wenks and color {self.color}")


class dogs(pets):
  def __init__(self, color, legs,wenks):
    super().__init__(color, legs, wenks)
  
  def bark(self):
    print("Dogs bark bow bow !!!!!!!")


    

myAnimal = animals("white",5)
myDog = dogs("black",4,"No")
myDog.bark()