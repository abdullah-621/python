class Car:
  def __init__(self,brand, model):
    self.__brand = brand  # __brand is private
    self.__model = model


class ElectricCar(Car):
  def __init__(self, brand,model,battey):
    super().__init__(brand,model)

    self.battery = battey


myCar = Car("tesla", "model S")
EleCar = ElectricCar("toyota","M6","85KHM")

print(isinstance(myCar, Car))
print(isinstance(EleCar, ElectricCar))

  