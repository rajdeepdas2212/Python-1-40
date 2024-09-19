def Prime_number(lower_value,upper_value):
    for num in range(lower_value,upper_value+1):
        if num > 1:
            for i in range(2,num):
                if num % i == 0:
                    break
            else:
                print(f'Prime number is: {num}')

lower_range = int(input('Input the lower range: '))
upper_range = int(input('Input the upper range: '))
Prime_number(lower_range,upper_range)