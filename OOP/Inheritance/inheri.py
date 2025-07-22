class Employee:
  company = "Microsoft"

  def domain(self, name):
    print(f"This is the domain of {self.name}")


class Programmer(Employee):
  company = "Google"

  def work(self):
    print(f"He work at {self.name}")

q = Employee()

print(q)