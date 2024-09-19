x = int(input('Enter the range of the series: '))
n1 = 0
n2 = 1
print(f'{n1}',end = " ")
print(f'{n2}',end = " ")
sum = 0
for i in range(1,x):
    sum = n1 + n2
    print(f'{sum}',end = " ")
    n1 = n2
    n2 = sum