#defining functions for required arithmetic operations

def add(a, b):
    result = a + b
    return result

def sub(a, b):
    result = a - b
    return result

def mul(a, b):
    result = a*b
    return result

def div(a, b):
    if b == 0:
        return "Oops! cannot divide by zero. "
    result = a / b
    return result

#Operations choices
while True:

    print("\nThe operations are: ")
    print("+. Addition ")
    print("-. Subtraction ")
    print("*. Multiplication ")
    print("/. Division ")
    print("E. THE END ")


    operation = input("\nEnter the operator for the operation you want to perform: ")

    

    if operation == '+':
        a = float(input("Enter the first operand: "))
        b = float(input("Enter the second operand: "))
        print(f"The sum of {a} and {b} is {add(a,b)}")

    elif operation == '-':
        a = float(input("Enter the first operand: "))
        b = float(input("Enter the second operand: "))
        print(f"The difference of {a} and {b} is {sub(a,b)}")

    elif operation == '*':
        a = float(input("Enter the first operand: "))
        b = float(input("Enter the second operand: "))
        print(f"The product of {a} and {b} is {mul(a,b)}")

    elif operation == '/':
        a = float(input("Enter the first operand: "))
        b = float(input("Enter the second operand: "))
        print(f"The result of division of {a} and {b} is {div(a,b)}")

    elif operation == 'E':
        print("You've ended the program")
        quit()

    else:
        print("The input is invalid")
        