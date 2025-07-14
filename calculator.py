number1 =int(input("enter first number: "))
number2 = int(input("enter second number: "))
operation = input("""
Enter operation No. to Perform: 
    1. Add
    2. Subtract
    3. Multiply
    4. Divide
    """)
def add(num1, num2):
    return num1+num2

def subtract(num1, num2):
    return num1-num2

def multiply(num1, num2):
    return num1*num2

def divide(num1, num2):
    return num1/num2

if(operation=='1' or operation=='+'):
    print(add(number1+number2))
elif(operation=='2' or operation=='-'):
    print(number1-number2)
elif (operation == '3' or operation=='*'):
    print(number1 * number2)
elif(operation=='4' or operation=='/'):
    print(number1/number2)
else:
    print("Invalid operator")
