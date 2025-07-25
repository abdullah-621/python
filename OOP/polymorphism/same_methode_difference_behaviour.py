class Car:
  def __init__(self,brand, model):
    self.__brand = brand  # __brand is private
    self.model = model
  
  def fuel_type(self):
    return "diesel or petrol"



class ElectricCar(Car):
  def __init__(self, brand,model,battey):
    super().__init__(brand,model)
    self.battery = battey

  def fuel_type(self):
    return "battery or charge"


myCar = Car("BMW", "X5")
EleCar = ElectricCar("Toyota","Y5","85KWH")

print(myCar.fuel_type())
print(EleCar.fuel_type())

  