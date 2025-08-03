import math

class circle:
  def __init__(self,radius):
    self.radius = radius

  def circle_area(self):
    return math.pi * self.radius**2
  
  def circle_perimeter(self):
    return 2 * math.pi * self.radius
  

c1 = circle(5)
area = c1.circle_area()
perimeter = c1.circle_perimeter()
print(f"Circle area : {area}")
print(f"Circle perimeter : {perimeter}")

    
