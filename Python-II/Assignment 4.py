#this is an advanced version of code with dynamic stock management.

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def addstock(self, quantity):
        self.quantity = self.quantity + quantity
        print(str(quantity) + " units of " + self.name + " added to inventory.\nCurrent Stock: " + str(self.quantity) + " units.")
    def sellstock(self, quantity):
        if(quantity > self.quantity):
            print("Only " + str(self.quantity) + "units are available in inventory.")
        else:    
            self.quantity = self.quantity - quantity
            print(str(quantity) + " units of " + self.name + " sold from inventory.\nCurrent Stock: " + str(self.quantity) + " units.")
    def viewstock(self):
        return self.price*self.quantity

class Category(Product):
    def __init__(self, name, category, price, quantity, discount=0):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category
        self.discount = discount
    def offer(self):
        return self.price * (1 - self.discount / 100) 
    
def main():
    product1 = Category("Laptop", "Electronics", 1000, 5, 5)
    product1.addstock(5)
    product1.sellstock(1)
    product1.viewstock()
    
main()    
