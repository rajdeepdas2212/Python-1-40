def leargest_number(list):
    max = list[0]
    for i in range(len(list)):
        if list[i] > max:
            max = list[i]
    return max

size = int(input("Enter the range of the list: "))
list = []
print(f'Input the elements:')
for i in range(size):
    element = int(input())
    list.append(element)
print(f'Smallest number is: {leargest_number(list)}')