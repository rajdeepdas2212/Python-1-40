def check_number(num):
    if num > 0:
        print(f'{num} this number is Posetive number')
    elif num == 0:
        print(f'{num} this number is Zero')
    else:
        print(f'{num} this number is Negetive number')

number = int(input('Enter the number: '))
check_number(number)