class ShoppingCart:
  def __init__(self):
    self.items = []

  def add_item(self, item_name, qty):
    item = (item_name,qty)
    self.items.append(item)
  
  
  def remove_item(self,item_name):
    flag = False
    for item in self.items:
      if item[0] == item_name:
        flag = True
        break
    if flag :
      print("Removed",item_name)
      self.items.remove(item)
      t = self.calculate_total()
      print(f"Now total price :",t)
    else:
      print("Items not found")
  def calculate_total(self):
    total = 0
    for item in self.items:
      total += item[1]
    return total
  

cart = ShoppingCart()
cart.add_item("papaya",100);
cart.add_item("guava",200);
cart.add_item("orange",300);

print("Current Items in Cart:")
for item in cart.items:
  print(item[0], "=", item[1],"TK")

print("---------------------")
total_qty = cart.calculate_total()
print("Total price :",total_qty,"TK")

cart.remove_item("orange")



