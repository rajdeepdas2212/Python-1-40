def prime_list(list):
    for i in range(len(list)):
        if list[i] < 0:
            print(f'Nega5tive number is: {list[i]}')
        elif list[i] == 0:
            print(f'This number is: Zero')
        else:
            continue

size = int(input('Enter the range of the list: '))
list = []
print(f'Input the elements: ')
for i in range(size):
    element = int(input())
    list.append(element)
prime_list(list)