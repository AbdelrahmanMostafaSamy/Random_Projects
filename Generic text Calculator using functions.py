#=======================================================
#Inputs for symbol and numbers:

order = input("Please input the order, EX:Add, Subtract, Divide, Multiply, Power: ").lower()
n1 = float(input("Please input the first number: "))
n2 = float(input("Please input the second number: "))
#===================
#The functions for add, subtract, divide, multiply and power:
#===================
def add(n1,n2):
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2
def divide(n1,n2):
    return n1 / n2
def multiply(n1,n2):
    return n1 * n2
def power(n1,n2):
    return n1 ** n2
#===================
#The if commands for the add, subtract, divide, multiply and power functions:
#===================
if order == "add":
    result = add(n1,n2)
elif order == "subtract":
    result = subtract(n1,n2)
elif order == "divide":
    result = divide(n1,n2)
elif order == "multiply":
    result = multiply(n1,n2)
elif order == "power":
    result = power(n1,n2)
    
print(f"The result is: {result}")
