# Simple Calculator (Add, Subtract, Multiply, Divide)
def Calculator(x,y, operation):
    if operation == "+":
        return x + y
    elif operation == "-":
        return x - y
    elif operation == "*":
        return x * y
    elif operation == "/":
        return x / y
    else:
        return "Invalid operation"
    
a = int(input("Enter the first number: "))
b  = int(input("Enter the second number: "))
op = input("Enter the wanted operation (+, -, *, /)")
result = Calculator(a, b , op)
print(f"Result: {result} ")
    
