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
            print(f"Product Name: {self.name}\nProduct Category: {self.category}\nProduct Price: {self.price}\nCurrent Stock: {self.quantity} | Value: {self.price*self.quantity}")

class Category(Product):
    def __init__(self, name, category, price, quantity, discount=0):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category
        self.discount = discount
    def offer(self):
        print(f"Product Name: {self.name}\nDiscount Percent: {self.discount} | Discounted Price: {(self.price - ((self.price*self.discount)/100))}")
    
def main():
    products = []
    while True:
        print("\n\nAvailable Choices:\n1. Add Item\n2. Add Stock\n3. Sell Stock\n4. View Stock\n5. Offer Price\n6. Remove Item\n7. Exit")
        val = int(input("Select your choice:\n"))
        if(val == 1):
            pname = input("Enter Product Name:")
            pcategory = input("Enter Product Category:")
            pprice = int(input("Enter Product Price:"))
            pstock = int(input("Enter Product Quantity:"))
            poffer = int(input("Enter Product Discount:"))
            pproduct = Category(pname, pcategory, pprice, pstock, poffer)
            products.append(pproduct)
        elif(val == 2):
            print("Current Items in inventory: ")
            for i in range(len(products)):
                product = products[i]
                print(f"{i + 1}. {product.name}")
            aval = int(input("Select the product: "))
            astock = int(input("Enter quantity to add: "))
            products[aval-1].addstock(astock)
        elif(val == 3):
            print("Current Items in inventory: ")
            for i in range(len(products)):
                product = products[i]
                print(f"{i + 1}. {product.name}")
            aval = int(input("Select the product: "))
            astock = int(input("Enter quantity to sell: "))
            products[aval-1].sellstock(astock)
        elif(val == 4):
            print("Current Items in inventory: ")
            for i in range(len(products)):
                product = products[i]
                print(f"{i + 1}. {product.name}")
            aval = int(input("Select the product: "))
            products[aval-1].viewstock()
        elif(val == 5):
            print("Current Items in inventory: ")
            for i in range(len(products)):
                product = products[i]
                print(f"{i + 1}. {product.name}")
            aval = int(input("Select the product: "))
            products[aval-1].offer()
        elif(val == 6):
            print("Current Items in inventory: ")
            for i in range(len(products)):
                product = products[i]
                print(f"{i + 1}. {product.name}")
            aval = int(input("Select the product: "))
            print(f"All units of {products[aval-1].name} removed from Inventory.")
            products.pop(aval-1)
        elif(val == 7):
                  print("Have a Nice Day!")
                  break
        else:
                  print("Invalid Choice!")      
main()    

# Basic Version:
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def addstock(self, amount):
        self.quantity = self.quantity + amount
        print(str(amount) + " " + self.name + " added to inventory. New Stock: " + str(self.quantity) + " Units.")
        
    def sellstock(self, amount):
        if(amount > self.quantity):
            print("Only " + str(self.quantity) + " units available in inventory.")
        else: 
            self.quantity = self.quantity - amount
            print(str(amount) + " " + self.name + " sold from inventory. New Stock: " + str(self.quantity) + " Units.")
            
    def viewstock(self):
        print("Available Units: " + str(self.quantity) + "\nEstimated Value: " + str(self.quantity*self.price))

class Category(Product):
    def __init__(self, name, category, price, quantity, discount=0):
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity    
        self.discount = discount

    def offer(self):
        print("Discounted price at " + str(self.discount) + "% discount is: " + str(self.price - ((self.price*self.discount)/100)))

def main():
    product1 = Category("Laptop", "Electronics", 1000, 5, 5)
    product1.offer()
    product1.addstock(5)
    product1.sellstock(2)
    product1.viewstock()

main()
