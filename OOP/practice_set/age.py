from datetime import date

class person:
  def __init__(self,name,country,dateOfBirth):
    self.name = name
    self.country = country
    self.dateOfBirth = dateOfBirth

  def age_calculator(self):
    return f"Name : {self.name}\nCountry : {self.country}\nAge : {date.today().year - self.dateOfBirth.year}"
  

p = person("Abdullah AL Masum","Bangladesh",date(2003,8,3))

age = p.age_calculator()
print(age)


