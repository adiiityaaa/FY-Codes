# This is a Basic version of Code without specialization:

class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def get_category(self):
        return "General Food"
class Fruit(Food):
    def get_category(self):
        return "Fruit"
class Vegetable(Food):
    def get_category(self):
        return "Vegetable"
class Dessert(Food):
    def get_category(self):
        return "Dessert"
    
apple = Fruit("Apple", "100")    
icecream = Dessert("Ice-Cream", "50")    
brinjal = Vegetable("Brinjal", "30")    
print("Apple Category is: " + apple.get_category() + ". Price: " + str(apple.price))
print("Icecream Category is: " + icecream.get_category() + ". Price: " + str(icecream.price))
print("Brinjal Category is: " + brinjal.get_category() + ". Price: " + str(brinjal.price))
