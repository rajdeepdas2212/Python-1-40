def even_list(list):
    for i in range(len(list)):
        if list[i] % 2 == 0:
            print(f'Even number is: {list[i]}')

size = int(input('Enter the range of the list:'))
list = []
print(f'Input the elements:')
for i in range(size):
    element = int(input())
    list.append(element)
even_list(list)