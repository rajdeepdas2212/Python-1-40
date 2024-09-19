def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def  multi(a,b):
    return a * b

def div(a,b):
    return a / b

num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the secound number: '))

print('Press 1: Addition')
print('Press 2: Subtraction')
print('Press 3: Multiplication')
print('Press 4: Division')

choice = int(input('Enter your choice: '))

if choice == 1:
    ans = add(num1,num2)
    print(f'Additon of the two numbers: {ans}')

elif choice == 2:
    ans = sub(num1,num2)
    print(f'Subtraction of the two numbers: {ans}')

elif choice == 3:
    ans = multi(num1,num2)
    print(f'Multiplication of the two numbers: {ans}')

elif choice == 4:
    ans = div(num1,num2)
    print(f'Division of the two numbers: {ans}')

else:
    print('Wrong Choice')
    
    print('Please try again')