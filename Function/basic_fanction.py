# Function define করার সময় → Parameter

# Function call করার সময় → Argument


#basic function
def my_function(name1 , name2):
  print(f"Hi {name1} ! Hi {name2}")


my_function("masum","noman")


# do not know how many arguments
# the function will receive a tuple of arguments

def you_function(*nums):
  print("Hello", nums[2])

you_function("masum","noman","shafi")  


# Keyword Arguments
# argument গুলোর নাম অবশ্যই parameter এর নামের সঙ্গে মিলতে হবে

def his_function(child3, child1, child2):
  print("His name is",child1)
  print("His name is",child2)
  print("His name is",child3)

his_function(child1 = "Harry" , child2 = "Akash", child3 = "Nipu")


# Arbitrary Keyword Arguments
# do not know how many keyword arguments that will be passed into your function
# the function will receive a dictionary of arguments

def her_function(**child):
  print("His name is", child["child1"])

her_function(child1 = "masum", child2 = "shafi")


