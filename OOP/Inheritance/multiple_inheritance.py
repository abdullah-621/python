class Employee:

  company = "Microsoft"
  name = "Abdullah"

  def domain(self):
    print(f"This is the domain of {self.name}")



class Gender:
   def gen(self):
     print(f"{self.name} is a Male")



class Programmer(Employee, Gender): # Multiple Inheritance
  company = "Google"

  def work(self):
    print(f"He work at {self.company}")



q = Programmer()
q.domain()
q.gen()
q.work()