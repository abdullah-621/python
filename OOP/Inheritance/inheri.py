class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, myname, shename, youname):
        super().__init__(myname, shename)
        self.youname = youname
    def Display(self):
        print(self.firstname, self.lastname)  # ✅ parent class এর variable use করো

x = Student("Mike", "Olsen", "hasu")
x.printname()   # Output: Mike Olsen
x.Display()     # Output: Mike Olsen
print(x.firstname)