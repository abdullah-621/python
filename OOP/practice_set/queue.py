# class Queue:
#   def __init__(self):
#     self.items = []
  
#   def is_empty(self):
#     return len(self.items) == 0

#   def is_size(self):
#     return len(self.items)
  
#   def enqueue(self,val):
#     print("dequeue",val)
#     self.items.append(val)
   
#   def dequeue(self):
#     if not self.is_empty():
#       print("enqueue",self.items[0])
#       self.items.pop(0)
#     else:
#       print("queue already empty !")

#   def display(self):
#     print(self.items)

# queue = Queue()
# queue.enqueue(10)
# queue.enqueue(20)
# queue.enqueue(30)
# queue.dequeue()
# queue.dequeue()
# queue.dequeue()

# print(queue.is_empty())
# queue.dequeue()


a = [1,2,3,4]

for i in range(4):
  print(a[0])
  a.pop(0)
  print(a)