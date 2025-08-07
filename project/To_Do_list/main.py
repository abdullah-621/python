import json
import os

class To_Do_List:
  def __init__(self):
    self.tasks = []
    # self.load_from_file()
    

  def show_menu(self):
    print("\n====== To-Do List Menu ======")
    print("1️⃣  Add Task")
    print("2️⃣  View Tasks")
    print("3️⃣  Delete Task")
    print("4️⃣  Mark Task as Done")
    print("5️⃣  Exit")
    print("=============================")


  def add_task(self):
    task = input("Enter new task :")
    self.tasks.append({"task":task, "status":"Not Done"})
    self.save_to_file()  # save to file
    print(f"{task} added successfully")
  
  def view_task(self):
    if not self.tasks:
      print("No task to show")
    else:
      print("\n==============\n")
      for i,task in enumerate(self.tasks,start=1):
        print(f"{i}.{task['task']} [{task['status']}]")
      print("\n==============\n")

  def mark_down(self):
    self.view_task()
    try:
      index = int(input("Enter task number which is complete :"))
      if 1 <= index <= len(self.tasks):
        self.tasks[index - 1]['status'] = "Done"
        self.save_to_file()
        print("Task mark as Done.")
      else:
        print("Invalid task number.")
    except ValueError:
      print("Please inter valid input.") 


  def delete_task(self):
    self.view_task()
    try:
      index = int(input("Enter task number to delete :"))
      if 1 <= index <= len(self.tasks):
        removed = self.tasks.pop(index - 1)
        self.save_to_file()
        print(f"Task {removed['task']} deleted")
      else:
        print("Invalid task number")

    except ValueError:
      print("Please enter a valid number.")

  def save_to_file(self,fileName = "main.json"):
    with open(fileName,'w') as f:
      json.dump(self.tasks,f,indent = 2)

  # def load_from_file(self, filename="tasks.json"):
  #   if os.path.exists(filename):
  #     with open(filename, "r") as f:
  #       self.tasks = json.load(f)
  #   else:
  #     self.tasks = []
    


List = To_Do_List()

while True:
  List.show_menu()
  try:
    chose = int(input("Chose an option (1-5) :"))
  except ValueError:
    print("Invalid input. please enter a number.")
    continue

  if(chose == 1):
    List.add_task()

  elif(chose == 2):
    List.view_task()

  elif(chose == 3):
    List.delete_task()

  elif(chose == 4):
    List.mark_down()
  
  else:
    print("Goodbye !")
    break
    