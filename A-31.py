def smallest_number(list):
    min = list[0]
    for i in range(len(list)):
        if list[i] < min:
            min = list[i]
    return min

size = int(input("Enter the range of the list: "))
list = []
print(f'Input the elements:')
for i in range(size):
    element = int(input())
    list.append(element)
print(f'Smallest number is: {smallest_number(list)}')