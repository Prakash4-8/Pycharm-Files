class Car:
    def __init__(self, make, model, year, weight):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight


car1 = Car('Hyundai', 'Swift', 2018, 123)
car2 = Car('Alto', 'Rover', 2019, 453)

print(car1.__dict__)
print(car2.__dict__)

print('My Favourite Car is', car2.make, car2.model)
