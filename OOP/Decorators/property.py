# @property ডেকোরেটরের কাজ হলো একটি মেথডকে অবজেক্টের প্রপার্টি (attribute)-এর মতো ব্যবহার করতে দেওয়া, অর্থাৎ এমনভাবে ব্যবহার করা যাতে () ছাড়া কল করা যায়, কিন্তু ভিতরে লজিক থাকে।

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def area(self):
        return 3.1416 * self._radius ** 2


c = Circle(5)
print(c.area)  # এখানে method কে call করিনি, কিন্তু value পেয়ে গেছি!



# class Car:
#   def __init__(self,brand, model):
#     self.__brand = brand  # __brand is private
#     self.__model = model

#   @staticmethod  # staticmethod no any self
#   def displayCar():
#     print(f"Car brand and Model")

#   @property  # property decorators insure that you can not overwrite this model
#   def model(self):
#     return self.__model



# class ElectricCar(Car):
#   def __init__(self, brand,model,battey):
#     super().__init__(brand,model)

#     self.battery = battey


# myCar = Car("tesla", "model S")
# # myCar.model = "masum"
# print(myCar.model)  # property decorators call it attribute not method

  




