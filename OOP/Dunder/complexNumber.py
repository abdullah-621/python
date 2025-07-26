class complex:
  def __init__(self,real,img):
    self.real = real
    self.img = img

  def showComplex(self):
    print(f"{self.real}i + {self.img}j")

  def __add__(self,num2):
    newReal = self.real + num2.real
    newImg = self.img + num2.img
    return complex(newReal , newImg)



num1 = complex(2,4)
num1.showComplex()

num2 = complex(4,2)
num2.showComplex()

print("-------")
# num3 = num1.add(num2)
# num3.showComplex()

num3 = num1 + num2
num3.showComplex()