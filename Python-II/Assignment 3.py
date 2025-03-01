#dynamic version with selective class:
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
class Student(Person): 
    def studies(self):
        print("\nI am " + self.name + ".")
        print("I like to study.")
class Teacher(Person):
    def teaches(self):
        print("I am " + self.name + ".")
        print("I like to teach.")

def main():
    name = input("Enter your name: \n")
    age = int(input("Enter your age:\n"))
    gender = input("Enter your gender\n")
    print("Available Choices:\n1. Student\n2. Teacher")
    val = int(input("Select your choice:\n"))
    if(val == 1):
        x = Student(name, age, gender)
        x.studies()
    elif(val == 2):
        y = Teacher(name, age, gender)
        y.teaches()
    else:
        print("Invalid Choice, Dummy.")
 
main()

#basic version with defined object:
class Person:
    def __init__(self, age, gender):
        self.age = age
        self.gender = gender
class Student(Person): 
    def studies(self):
        print("I study.")
class Teacher(Person):
    def teaches(self):
        print("I teach.")

x = Student("18", "Male")
x.studies()
y = Teacher("40", "Female")
y.teaches()
