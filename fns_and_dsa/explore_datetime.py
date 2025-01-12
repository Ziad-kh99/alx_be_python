from datetime import datetime, timedelta

def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()

    # Format current date and time like 'YYYY-MM-DD HH:MM:SS'
    # formatted_dt = current_date.strftime('%Y-%m-%d %H:%M:%S')

    print('Current date and time:', current_date.strftime('%Y-%m-%d %H:%M:%S'))

def calculate_future_date():
    try:
        number_of_days = int(input('Enter the number of days to add to the current date: '))
    except:
        print('Invlid parsing operations, please enter a valid number.')
        exit()

    current_date = datetime.now()
    future_date = current_date + timedelta(days=number_of_days)
    
    print('Future date:', future_date.strftime('%Y-%m-%d'))


