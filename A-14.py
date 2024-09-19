def area(radius):
    area = 3.14 * (radius ** 2)
    return area

radius = int(input('Input the radius of the circle: '))
print(f'Area of the circle is: {area(radius)}')