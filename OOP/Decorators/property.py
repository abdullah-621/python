class Car:
  def __init__(self,brand, model):
    self.__brand = brand  # __brand is private
    self.__model = model

  @staticmethod  # staticmethod no any self
  def displayCar():
    print(f"Car brand and Model")

  @property  # property decorators insure that you can not overwrite this model
  def model(self):
    return self.__model



class ElectricCar(Car):
  def __init__(self, brand,model,battey):
    super().__init__(brand,model)

    self.battery = battey


myCar = Car("tesla", "model S")
myCar.model = "masum"
print(myCar.model)  # property decorators call it attribute not method

  