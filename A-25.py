row = int(input("Enter the row of the matrix: "))
column = int(input("Enter the column of the matrix: "))
print(f'Input the {row * column} numbers:')
matrix = []
for i in range(row):
    m =[]
    for j in range(column):
        element = int(input(f'Matrix[{i}][{j}] = '))
        m.append(element)
    matrix.append(m)
trans = []
for i in range(row):
    result =[]
    for j in range(column):
        result.append(matrix[j][i])
    trans.append(result)
print(f'Original matrix')
for i in matrix:
    print(i)
print(f'Transposed of a matrix')
for i in trans:
    print(i)