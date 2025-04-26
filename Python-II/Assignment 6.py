# Basic version of the code:
try: 
    num1 = input("Enter the first number:\n")
    num2 = input("Enter the second number:\n")
    if not num1.isdigit() or not num2.isdigit():
        raise TypeError("Input must be a number.")
    else:
        num1 = int(num1)
        num2 = int(num2)
        sum = num1+num2
        diff = num1-num2
        pro = num1*num2
        div = num1/num2
        print(f"Addition: {sum}\nSubtraction: {diff}\nMultiplication: {pro}\nDivision: {div}")
except TypeError as e:
    print(f"An error occured: {e}")
