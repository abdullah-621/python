# class employee:
  
#   def putdata(self):
#     id = int(input("Enter your ID : "))
#     self.name = (input("Enter your name : "))
#     self.salary = float(input("Enter your salary : "))

#   def display(self):
#     print("Emplyee id : ", self.id)
#     print("Emplyee nmae : ", self.name)
#     print("Emplyee salary : ", self.salary)


# a = employee()
# a.putdata()
# a.display()


# class Employee:
#     id = None
#     name = ""
#     salary = 0.0

#     def putdata(self):
#         Employee.id = int(input("Enter your ID: "))
#         Employee.name = input("Enter your name: ")
#         Employee.salary = float(input("Enter your salary: "))

#     def display(self):
#         print("ID:", Employee.id)
#         print("Name:", Employee.name)
#         print("Salary:", Employee.salary)


# a = Employee()
# b = Employee()

# a.putdata()   # তুমি এখানে input দাও
# a.display()
# b.display()   # এটা একই ডেটা দেখাবে, কারণ class variable সবার জন্য একই





class Employee:
    def __init__(self, id=None, name="", ary=0.0):
        self.id = id
        self.name = name
        self.salary = ary

    # def putdata(self):
    #     self.id = int(input("Enter your ID: "))
    #     self.name = input("Enter your name: ")
    #     self.salary = float(input("Enter your salary: "))

    def display(self):
        print("ID:", self.id)
        print("Name:", self.name)
        print("Salary:", self.salary)

a = Employee()
b = Employee(9,"h",80)
# a.putdata()
b.display()
