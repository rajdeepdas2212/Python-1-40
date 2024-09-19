def rever_list(list):
    new_list = []
    new_list = list[::-1]    
    return new_list

size = int(input("Enter the range of the list: "))
list = []
print(f'Input the elements: ')
for i in range(size):
    element = int(input())
    list.append(element)
print(f'Reversing of the list is: {rever_list(list)}')