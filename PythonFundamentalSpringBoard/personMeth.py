class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age= age
        self.height = height
    def speaK(self):
        print('Hello, My name is {}. I am {} year old.'.format(self.name, self.age))
    def greet(self, person):
        if person.name == "prakash":
            print('Hi neighbour')
        else:
            print('Hi {}'.format(person.name))

prakash = Person('Vikash', 23, 234)
prakash.greet(prakash)