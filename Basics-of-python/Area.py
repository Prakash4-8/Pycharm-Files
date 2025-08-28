def area(a, *b):
    if len(b) == 0:
        return a * a
    elif len(b) == 1:
        return a * b[0]
    s = (a + b[0] + b[1]) / 2
    return (s * (s - a) * (s - b[0]) * (s - b[1])) ** 0.5


def calc_area(x):
    if x == 1:
        print('Enter triangle\'s length of')
        a = float(input('Side 1 : '))
        b = float(input('Side 2 : '))
        c = float(input('Side 3 : '))
        if a <= 0 or b <= 0 or c <= 0:
            input('Wrong input!')
            exit()
        print('Area of the triangle = ', area(a, b, c), 'sq. units')
    elif x == 2:
        a = float(input('Enter length of a side of the square : '))
        if a <= 0:
            input('Wrong input!')
            exit()
        print('Area of the square = ', area(a), 'sq. units')
    else:
        a = float(input('Enter length of the rectangle : '))
        b = float(input('Enter breadth of the rectangle  : '))
        if a <= 0 or b <= 0:
            input('Wrong input!')
            exit()
        print('Area of the square = ', area(a, b), 'sq. units')