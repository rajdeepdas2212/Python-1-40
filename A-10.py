def largest_number(a,b,c):
    if a > b and a > c:
        print(f'Leargest number is: {a}')
    elif b > a and b > c:
        print(f'Leargest number is: {b}')
    else:
        print(f'Leargest number is: {c}')

num1 = int(input('Enter the 1st number: '))
num2 = int(input('Enter the 2nd number: '))
num3 = int(input('Enter the 3rd number: '))
largest_number(num1,num2,num3)