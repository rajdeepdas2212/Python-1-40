def sum_of_array(array,n):
    sum = 0
    for i in range(n):
        sum += array[i]
    return sum

size = int(input('Enter the range of an array: '))
array = []
print(f'Enter the array elements: ')
for i in range(size):
    element = int(input())
    array.append(element)
print(f'Sum of the array is: {sum_of_array(array,size)}')