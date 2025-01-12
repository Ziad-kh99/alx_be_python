FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


try:
    temp = int(input('Enter the temperature to convert: '))
except:
    print('Invalid temperature. Please enter a numeric value.')
    exit()

temp_unit = input('Is this temperature in Celsius or Fahrenheit? (C/F): ')

if temp_unit.strip().upper() == 'F':
    c_temp = convert_to_celsius(temp)
    print(f'{temp}°F is {c_temp}°C')

elif temp_unit.strip().upper() == 'C':
    f_temp = convert_to_fahrenheit(temp)
    print(f'{temp}°C is {f_temp}°F')
else:
    print('Invalid temperature unit.') 
    exit()


