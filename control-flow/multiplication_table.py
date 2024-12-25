try:
    number = int(input('Enter a number to see its multiplication table: '))
except:
    print('Please enter an invalid number')
    exit()

for n in range(1, 11):
    print(f'{number} * {n} = {number * n}')
