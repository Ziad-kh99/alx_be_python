try:
    size = int(input('Enter the size of the pattern: '))
except:
    print('Invalid integer!')
    exit()

temp_size = size

while size > 0:
    for n in range(0, temp_size):
        print('*', end='')
    print()
    size -= 1

