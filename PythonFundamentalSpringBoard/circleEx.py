class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def circumference(self):
        return 2 * 3.14 * self.radius

    def change_radius(self, new_radius):
        self.radius = new_radius


circle1 = Circle(1)
while True:
    radius = input('please enter radius: ')
    if radius == 'sa':
        break
    elif not(radius.isalpha()):
        circle1.change_radius(int(radius))
        print('Area: ', circle1.area())
        print('Circumference: ', circle1.circumference())


