def swap(a,b):
    a = a+b
    b = a-b
    a = a-b
    print(f'After the swap {a} and {b}')
    
a = int(input('Input the a value: '))
b = int(input('Enter the b value: '))
print(f'Before the swap {a} and {b}')
swap(a,b)