#this is an advanced and dynamic version of the code which allows the user to specify length or breadth for specific shape.

def tarea(b, h,u):
    a = 0.5*b*h
    print("\nArea of Triangle is " + str(a) + "sq. " + str(u))
def sarea(s,u):
    a = s*s
    print("\nArea of Square is " + str(a) + "sq. " + str(u))
def carea(r,u):
    a = 3.14*r*r
    print("\nArea of Circle is " + str(a) + "sq. " + str(u))
def rarea(l, b,u):
    a = l*b
    print("\nArea of Rectangle is " + str(a) + "sq. " + str(u))
def tper(x, y, z,u):
    a = x+y+z
    print("\nPerimeter of Triangle is " + str(a) + str(u))
def sper(s,u):
    a = 4*a
    print("\nPerimeter of Square is " + str(a) + str(u))
def cper(r,u):
    a = 2*3.14*r
    print("\nPerimeter of Circle is " + str(a) + str(u))
def rper(l, b,u):
    a = 2*(l+b)
    print("\nPerimeter of Rectangle is " + str(a) + str(u))

def main():
    u = input("Enter the unit:\n")
    oval = int(input("Select the Operation:\n1. Perimeter of Shape\n2. Area of Shape\n"))
    sval = int(input("Select the Shape:\n1. Circle\n2. Rectangle\n3. Square\n4. Triangle\n"))
    if(oval == 1):
        if(sval == 1):
            o = int(input("Enter the radius of circle:"))
            cper(o, u)
        elif(sval == 2):
            o = int(input("Enter the length of rectangle:"))
            p = int(input("Enter the breadth of rectangle:"))
            rper(o, p, u)
        elif(sval == 3):
            o = int(input("Enter the side of the square:"))
            sper(o, u)
        elif(sval == 4):
            o = int(input("Enter the first side of triangle:"))
            p = int(input("Enter the second side of triangle:"))
            q = int(input("Enter the third side of triangle:"))
            tper(o,p,q,u)
        else:
            print("Invalid Choice")
    elif(oval == 2):
        if(sval == 1):
            o = int(input("Enter the radius of circle:"))
            carea(o,u)
        elif(sval == 2):
            o = int(input("Enter the length of rectangle:"))
            p = int(input("Enter the breadth of rectangle:"))
            rarea(o, p, u)
        elif(sval == 3):
            o = int(input("Enter the side of the square:"))
            sarea(o,u)
        elif(sval == 4):
            o = int(input("Enter the height of triangle:"))
            p = int(input("Enter the base of triangle:"))
            tarea(o, p,u)
        else:
            print("Invalid Choice")
    else:
        print("Invalid Choice.")
        
main()        

# Basic version of the code via ChatGPT based on Pseudocode
import math
class ShapeCalculations:
    def triangle_calculations(self, a, b, c):
        s = (a + b + c) // 2  
        area = int(math.sqrt(s * (s - a) * (s - b) * (s - c)))
        perimeter = a + b + c
        return area, perimeter
    def rectangle_calculations(self, length, width):
        area = length * width
        perimeter = 2 * (length + width)
        return area, perimeter
    def circle_calculations(self, radius):
        area = int(3.14 * radius ** 2)
        circumference = int(2 * 3.14 * radius)
        return area, circumference
    def square_calculations(self, side):
        area = side ** 2
        perimeter = 4 * side
        return area, perimeter

def main():
    calc = ShapeCalculations()
    tri_area, tri_perimeter = calc.triangle_calculations(3, 4, 5)
    print(f"Triangle Area: {tri_area}, Perimeter: {tri_perimeter}")
    rect_area, rect_perimeter = calc.rectangle_calculations(10, 5)
    print(f"Rectangle Area: {rect_area}, Perimeter: {rect_perimeter}")
    circ_area, circ_circumference = calc.circle_calculations(7)
    print(f"Circle Area: {circ_area}, Circumference: {circ_circumference}")
    sq_area, sq_perimeter = calc.square_calculations(6)
    print(f"Square Area: {sq_area}, Perimeter: {sq_perimeter}")

main()
