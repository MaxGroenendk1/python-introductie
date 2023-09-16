#rekenmachine

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

x = float(input("give first number: "))
y = float(input("give second number: "))
operator = input("declare operator [+,-,*,/]: ")
if(operator == "+"):
    print(add(x, y))
if(operator == "-"):
    print(subtract(x, y))
if(operator == "*"):
    print(multiply(x, y))
if(operator == "/"):
    print(divide(x, y))
    