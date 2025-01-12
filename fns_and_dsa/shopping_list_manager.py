def display_menu():
    print('Shopping List Manager')
    print('1. Add Item')
    print('2. Remove Item')
    print('3. View List')
    print('4. Exit')

def main():
    shopping_list = []

    while True:
        display_menu()
        choice = input('Enter your choice: ')

        if choice == '1':
            item_name = input('Enter the item to add: ')
            shopping_list.append(item_name)
        elif choice == '2':
            item_name = input('Enter the item to remove: ')
            try:
                shopping_list.remove(item_name)
            except ValueError:
                print(f'The value {item_name} doesn\'t exist.')
        elif choice == '3':
            for item in shopping_list:
                print(item)
        elif choice == '4':
            print('Goodbye!')
            break
        else:
            print('Invalid choice. Please try again.')


if __name__ == "__main__":
    main()