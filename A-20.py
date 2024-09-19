def recur_fact(n):
    if n == 1:
        return n
    else:
        return n * recur_fact(n-1)

num = int(input('Enter the range: '))
print(f'{num}! Factorial is: {recur_fact(num)}')