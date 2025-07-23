class anonymous:
  a = 1

  @classmethod
  def show(cla):
    print("The value of a is : ", cla.a)

  @property
  def name(self):
    return f"{self.fname} {self.lname}"
  
  @name.setter
  def name(self, value):
    self.fname = value.split(" ")[0]
    self.lname = value.split(" ")[1]


a = anonymous()
a.a = 45
a.name = "Harry khan al"
print(a.name)
a.show()