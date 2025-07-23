class Employee:

  company = "Microsoft"
  name = "Abdullah"

  def domain(self):
    print(f"This is the domain of {self.name}")



class Gender:
   def gen(self):
     print(f"{self.name} is a Male")


# Multiple Inheritance
class Programmer(Employee, Gender): 
  company = "Google"

  def work(self):
    print(f"He work at {self.company}")



q = Programmer()
q.domain()
q.gen()
q.work()