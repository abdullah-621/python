class Stack:
  def __init__(self):
    self.items = []

  def is_size(self):
    return len(self.items)
  
  def is_empty(self):
    return len(self.items) == 0
  
  def top(self):
    return self.items[len(self.items) - 1]

  def push(self,val):
    print("pushed",val)
    self.items.append(val)
  
  def pop(self):
    if not self.is_empty():
      print(f"Poped {self.top()} from stack")
      self.items.pop()
    else:
      print("Opps items is empty !")
    
  def display(self):
    print("Items :",self.items)

stack = Stack()
stack.push(12)
stack.push(13)
stack.push(14)
stack.pop()
stack.pop()
stack.pop()
print(stack.is_empty())
