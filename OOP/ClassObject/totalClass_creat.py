class Car:
  total_car = 0
  def __init__(self,brand, model):
    self.__brand = brand  # __brand is private
    self.model = model
    Car.total_car += 1
  
  def fuel_type(self):
    return "diesel or petrol"



class ElectricCar(Car):
  def __init__(self, brand,model,battey):
    super().__init__(brand,model)
    self.battery = battey

  def fuel_type(self):
    return "battery or charge"


Car("BMW", "X5")
Car("BMW", "X5")
Car("BMW", "X5")
ElectricCar("Toyota","Y5","85KWH")


print(Car.total_car)