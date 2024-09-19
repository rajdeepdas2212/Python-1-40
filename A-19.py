def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return recur_fibo(n-1) + recur_fibo(n-2)
    
num = int(input('Enter the range of the series: '))

if num <= 0:
    print(f'Please enter the posetive integer number')
else:
    for i in range(num+1):
        print(f'{recur_fibo(i)}',end = " ")