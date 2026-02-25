

def perform_action(num1, num2, action):
    if action == '+':
        return num1 + num2
    elif action == '-':
        return num1 - num2
    elif action == '/':
        return num1 / num2
    elif action == '*':
        return num1 * num2
    else:
        return "Action error!"

number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))
operand = str(input("Enter Operand: "))

result = perform_action(number1, number2, operand)

print(result)

if(result > 0): 
    print("Positive")
elif result < 0:
    print("Negative")
else:
    print("Zero")