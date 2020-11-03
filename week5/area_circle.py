def are_circle(radius):
    return 3.14 * (radius ** 2)


radius = int(input('Please enter the radius of the circle: '))
result = are_circle(radius)
print('The area of a circle with radius {} is {}'.format(radius,result))

