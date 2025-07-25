class Car:
  def __init__(self,brand, model):
    self.brand = brand
    self.model = model
   
  def displayCar(self):
    print(f"Car brand : {self.brand} and Model : {self.model}")

class ElectricCar(Car):
  def __init__(self, brand,model,battey):
    super().__init__(brand,model)

    self.battery = battey


myCar = Car("BMW", "X5")
# print(myCar.battery)
# print(myCar.brand,myCar.model)

EleCar = ElectricCar("Toyota","Y5","85KWH")
# print(EleCar.brand, EleCar.model, EleCar.battery)
print(myCar.displayCar())
  