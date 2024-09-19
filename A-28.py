def length_list(list):
    size = len(list)
    return size

size = int(input("Enter the range of the list: "))
list = []
print(f'Input the elements: ')
for i in range(size):
    element = int(input())
    list.append(element)
print(f'Length of the list is: {length_list(list)}')