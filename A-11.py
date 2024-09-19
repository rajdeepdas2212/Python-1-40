def factors(num):
    print(f'Factors are: ')
    for i in range(1,num+1):
        if num % i == 0:
            print(f'{i}')

number = int(input('Enter the number: '))
factors(number)