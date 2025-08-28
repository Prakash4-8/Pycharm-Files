# duck typing program
class HP:
    def fueling(self):
        print('Welcome to Hindustan Petrolium')
        print('Fueling Your Bike...')
        print("It's now ready to drive...")


class Reliance:
    def fueling(self):
        print('Welcome to Reliance Petrolium')
        print('Fueling Your Bike...')
        print("It's now ready to drive...")


class LetsFuel:
    def Do(self, company):
        company.fueling()


comp = HP()
s1 = LetsFuel()
s1.Do(comp)

# Abstract class
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def eating(self):
        pass


class Bird(Animal):
    def eating(self):
        print('The bird is eating now ...')


class1 = Bird()


# operator overloading
class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        r1 = self.m1 + other.m1
        r2 = self.m2 + other.m2

        s3 = Student(r1, r2)
        return s3


s1 = Student(2, 3)
s2 = Student(4, 5)

s3 = s1 + s2
print(s3.m2 + s3.m1)


