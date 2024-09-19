def sum_of_squares(n):
    sum = 0
    for i in range(1,n+1):
        sum += i ** 2
    return sum

num = int(input('Enter the range: '))
print(f'Sum of squares is: {sum_of_squares(num)}')