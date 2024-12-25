try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
except: 
    print('Please enter an invalid number.')
    exit()

operation = input("Choose the operation (+, -, *, /): ")


match operation:
    case '+':
        result = num1 + num2
    case '-':
        result = num1 - num2
    case '*':
        result = num1 * num2
    case '/':
        try:
            result = num1 / num2
        except:
            print('Cannot divide by zero.') 
            exit()
    case _:
        print('Invalid Operation.')
        exit()

print(f'The result is {result}')

