try:
    number = int(input('Enter a number to see its multiplication table: '))
except:
    print('Please enter an invalid number')
    exit()

table_range = list(range(1,11))

for n in table_range:
    print(f'{number} * {n} = {number * n}')
