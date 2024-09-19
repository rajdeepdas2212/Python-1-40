def swap_list(list):
    print(f'After the swap list: \n{list}')
    temp = list[0]
    list[0] = list[len(list)-1]
    list[len(list)-1] = temp
    return list

size = int(input('Enter the range of the list: '))
list = []
print(f'Input the elements: ')
for i in range(size):
    element = int(input())
    list.append(element)
print(f'After the swap list: \n{swap_list(list)}')