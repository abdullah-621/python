class programmer:
  
  company = "microsoft"
  def __init__(self, name, salary, work):
    
    self.name = name
    self.salary = salary
    self.work = work
    

p = programmer("Abdullah Al Masum", "ML Engineer", 120000)
q = programmer("Shafiqul Islam", "Softwore Engineer", 120000)

print(p.name, p.work, p.salary)
print(q.name, q.work, q.salary)

