def swap_list(list):
    
    pos1 = int(input("Enter the first position of the list: "))
    pos2 = int(input("Enter the second position of the list: "))
    
    print(f'Before the swap:\n{list}')
    temp = list[pos1-1]
    list[pos1-1] = list[pos2-1]
    list[pos2-1] = temp

    return list

size = int(input('Enter the range of the list: '))
list = []
print(f'Input the elements:')
for i in range(size):
    element = int(input())
    list.append(element)
print(f'After the swap:\n{swap_list(list)}')