row1 = int(input('Enter the row of the first matrix: '))
column1 = int(input('Enter the column of the first matrix: '))
print(f'Input the {row1 * column1} elements')
matrix1 = []
for i in range(row1):
    m1 = []
    for j in range(column1):
        element = int(input(f'Matrix[{i}][{j}] = '))
        m1.append(element)
    matrix1.append(m1)
row2 = int(input('Enter the row of the second matrix: '))
column2 = int(input('Enter the column of the second matrix: '))
print(f'Input the {row2 * column2} elements')
matrix2 = []
for i in range(row2):
    m2 = []
    for j in range(column2):
        element = int(input(f'Matrix[{i}][{j}] = '))
        m2.append(element)
    matrix2.append(m2)
print(f'First Matrix:')
for i in matrix1:
    print()
print(f'Second Matrix:')
for i in matrix2:
    print()
if column1 == row2:
    multiplication = []
    for i in range(row2):
        multi = []
        for j in range(column1):
            sum = 0
            for k in range(column2):
                sum += matrix1[i][k] * matrix2[k][j]
            multi.append(sum)
        multiplication.append(multi)
else:
    print(f'This matrix is not possible')
print(f'Matrix Multiplication:')
for i in multiplication:
    print()