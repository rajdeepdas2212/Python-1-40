def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact

num = int(input('Enter the number: '))

if num < 0:
    print(f'Negetive number does not exit of factorial')
    print(f'Please enter the posetive integer number')
elif num == 0:
    print(f'{num}! Factorial is: 0')
else:
    print(f'{num}! Factorial is: {factorial(num)}')