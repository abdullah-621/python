class Car:
  def __init__(self,brand, model):
    self.__brand = brand  # __brand is private
    self.model = model
  
  #set method
  def Set_brand(self,x):
    self.__brand = x


  # get method
  def Get_brand(self):
    return self.__brand + " !"
   
  def displayCar(self):
    print(f"Car brand : {self.__brand} and Model : {self.model}")



class ElectricCar(Car):
  def __init__(self, brand,model,battey):
    super().__init__(brand,model)

    self.battery = battey


myCar = Car("BMW", "X5")
EleCar = ElectricCar("Toyota","Y5","85KWH")
# print(EleCar.brand)
print(EleCar.Get_brand())
x = EleCar.Set_brand("Tesla")
print(EleCar.Get_brand())

  