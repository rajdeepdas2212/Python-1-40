def Armstrong_number(num):
    numof= len(str(num))
    term = num
    sum = 0
    while term > 0:
        digit = term % 10
        sum += digit ** numof
        term //= 10
    
    if sum == num:
        print(f'{num} This number is an Armstrong number')
    else:
        print(f'{num} This number is not an Armstrong number')

number = int(input('Enter the posetive interger number: '))
Armstrong_number(number)