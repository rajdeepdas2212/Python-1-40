def recur_sum(n):
    if n == 1:
        return n
    else:
        return n + recur_sum(n-1)

num = int(input('Enter the range: '))
print(f'Sum of the natural number is: {recur_sum(num)}')