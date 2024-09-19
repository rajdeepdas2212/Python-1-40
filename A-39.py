def sum(list):
    new_list = []
    sum = 0
    for i in range(len(list)):
        sum += list[i]
        new_list.append(sum)
    return new_list

size = int(input("Enter the range of the list: "))
list = []
for i in range(size):
    element = int(input())
    list.append(element)
print(f'Cumulative sum is: {sum(list)}')