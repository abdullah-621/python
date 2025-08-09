class Product:
  def __init__(self,name, price, quantity):
    self.name = name
    self.price = price
    self.quantity = quantity

  def get_total(self):
    return self.price * self.quantity
  
  def __str__(self):
    return f"{self.name} - {self.price} x {self.quantity} = {self.get_total()}"


class GroceryBilling:
  def __init__(self):
    self.cart = []
  
  def show_menu(self):
    print("\n===== Grocery Billing System =====")
    print("1. Add Product")
    print("2. Remove Product")
    print("3. Show cart")
    print("4. CheckOut")
    print("5. Exit")
  
  # private method
  def __total_price(self):
    total = sum(item.get_total() for item in self.cart)
    return total
   
  # private method
  def __add_discount(self,discount):
    total = self.__total_price()
    total_after_discount = total - (total * discount / 100)
    return total_after_discount
  
  # private method
  def __add_tax(self,tax,discount):
    total_after_discount = self.__add_discount(discount)
    total_after_tax = total_after_discount + (total_after_discount * tax / 100)
    return total_after_tax
  
  def add_product(self):
    name = input("Enter product name: ")
    price = float(input("Enter price per unit: "))
    quantity = int(input("Enter quantity: "))
    self.cart.append(Product(name,price,quantity))
    print(f"✅ {name} added to cart!\n")

  def rem_product(self):
    if not self.cart:
      print("Cart is empty!")
      return
    self.show_cart()
    try:
      index = int(input(f"Choose remove no(1-{len(self.cart)}):"))
      if 1 <= index <= len(self.cart):
        remove = self.cart.pop(index - 1)
        print(f"Removed {remove} from cart.")
      else:
        print("Invalid input.")
    except ValueError:
      print("Invalid input.")

  def show_cart(self):
    if not self.cart:
      print("🛒 Cart is empty.\n")
      return
    print("\n------ Cart Items ------")
    for idx, item in enumerate(self.cart,start=1):
      print(f"{idx}. {item}")
    print("------------------------")
    total = self.__total_price()
    print(f"Total (without discount/tax): {total} tk\n")
  
  def checkout(self):
    if not self.cart:
      print("🛒 Cart is empty.Add products first.\n")
      return
    
    total = self.__total_price()
    discount = float(input("Enter discount (%) : "))
    tax = float(input("Enter tax (%) : "))

    print("\n===== BILL =====")
    for item in self.cart:
      print(item)
    print("----------------")
    print(f"Total: {total} tk")
    print(f"After {discount}% discount: {self.__add_discount(discount):.2f} tk")
    print(f"Afetr adding {tax}:{self.__add_tax(tax,discount):.2f} tk")

    with open("bill.txt" ,'w') as f:
      f.write("===== BILL =====\n")
      for item in self.cart:
        f.write(str(item) + "\n")
      
      f.write("------------------------------\n")
      f.write(f"Total price : {self.__total_price()}")
      f.write(f"After {discount}% discount: {self.__add_discount(discount):.2f} tk\n")
      f.write(f"Afetr adding {tax}:{self.__add_tax(tax,discount):.2f} tk\n")
      f.write("Bill saved to bill.txt\n")

      f.write("Happy Shopping ! \nSee you Again !\n")


billing = GroceryBilling()

while True:
  billing.show_menu()
  try:
    Choose = int(input("Choose an option (1-5) :"))
  except ValueError:
    print("Invalid input. please enter a number.")
    continue

  if(Choose == 1):
    billing.add_product()

  elif(Choose == 2):
    billing.rem_product()

  elif(Choose == 3):
    billing.show_cart()

  elif(Choose == 4):
    billing.checkout()
  
  else:
    print("Goodbye !")
    break
    