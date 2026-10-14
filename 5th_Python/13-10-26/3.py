"""Create a Product class with the product name, price, and quantity.
Add an instance method to calculate the total cost.
Take these values from the user and display the product name and 
total cost.
"""

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_cost(self):
        return self.price * self.quantity

name = input("Enter Product Name : ")
price = float(input("Enter Product Price : "))
quantity = int(input("Enter Quantity : "))

p1 = Product(name, price, quantity)

print("Product Name :",p1.name)
print("Total Cost :",p1.total_cost())