def sum_list(list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    return sum

size = int(input("Enter the range of the list: "))
list = []
print(f'Input the elements: ')
for i in range(size):
    element = int(input())
    list.append(element)
print(f'Sum of the list: {sum_list(list)}')
