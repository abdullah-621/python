class Car:
  def __init__(self,brand, model):
    self.__brand = brand  # __brand is private
    self.model = model

  @staticmethod  # staticmethod no any self
  def displayCar():
    print(f"Car brand and Model")



class ElectricCar(Car):
  def __init__(self, brand,model,battey):
    super().__init__(brand,model)

    self.battery = battey


myCar = Car("tesla", "model S")
print(Car.displayCar())

  