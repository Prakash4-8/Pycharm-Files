class Cat:
    def __init__(self, mass, lifespan, speed):
        self.mass_in_kg = mass
        self.lifespan_in_year = lifespan
        self.speed_in_kph = speed

    def vocalize(self):
        print('meeeeooowww')

    def __str__(self):
        return f' the {type(self).__name__.lower()}' \
               f' weights {self.mass_in_kg} kg' \
               f' and lives for {self.lifespan_in_year} years' \
               f' and can run at a speed of {self.speed_in_kph} kph'


class Leopard(Cat):
    def __init__(self, mass, lifespan, speed, spotted=True):
        super().__init__(mass, lifespan, speed)  # method overriding is happening here
        self.spotted = spotted

        def vocalize(self):
            print('wwggghhhrrr')

    def __str__(self):  # method overriding is happeniing here
        if self.spotted == True:
            st = 'spotted '
        else:
            st = ''
        return f' the {st}{type(self).__name__.lower()}' \
               f' weights {self.mass_in_kg} kg' \
               f' and lives for {self.lifespan_in_year} years' \
               f' and can run at a speed of {self.speed_in_kph} kph'


class Cheetha(Cat):
    def vocalize(self):
        print('eeeeee')


tommy = Cat(2, 4, 4)
tommy.vocalize()
print(tommy)

leopard = Leopard(3, 5, 6, True)
leopard.vocalize()
print(leopard)

cheeta = Cheetha(3, 7, 2)
cheeta.vocalize()
print(cheeta)
