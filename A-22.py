def largest(array,n):
    max = array[0]
    for i in range(n):
        if array[i] > max:
            max = array[i]
    return max

size = int(input('Enter the range of the list: '))

list = []
print(f'Enter the elements: ')
for i in range(size):
    element = int(input())
    list.append(element)
print(f'Largest number is: {largest(list,size)}')