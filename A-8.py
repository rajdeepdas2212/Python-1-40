def Even_Odd(num):
    if num % 2 == 0:
        print(f'{num} This number is Even number')
    else:
        print(f'{num} This number is Odd number')

number = int(input('Enter the posetive integer number: '))
Even_Odd(number)