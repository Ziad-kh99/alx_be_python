def perform_operation(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2 
    elif operation == 'multiply':
        return num1 * num2 
    elif operation == 'divide':
        # try:
        #     return num1 / num2
        # except:
        #     print('Invalid division by Zero operation')
        if num2 == 0:
            print('Invalid division by Zero operation')
        else:
            return num1 / num2
    else:
        print('Invalid operation')