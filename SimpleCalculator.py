print("Simple Calculator")
num_1 = input("Enter your first number: ")
num_2 = input("Enter your second number: ")
ops = input("Choose the operator (+, -, *, /): ")

try:
    num_1 = float(num_1)
    num_2 = float(num_2)
    
    if ops == '+':
        result = num_1 + num_2
        print(f"{num_1} + {num_2} = {result}")
    elif ops == '-':
        result = num_1 - num_2
        print(f"{num_1} - {num_2} = {result}")
    elif ops == '*':
        result = num_1 * num_2
        print(f"{num_1} * {num_2} = {result}")
    elif ops == '/':
        if num_2 == 0:
            print("Error:- Cannot divide by zero!")
        else:
            result = num_1 / num_2
            print(f"{num_1} / {num_2} = {result}")
    else:
        print("Error:- Invalid ops! Please use +, -, *, or /")
        
except ValueError:
    print("Error:- Please enter valid numbers!")