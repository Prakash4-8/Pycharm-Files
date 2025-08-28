class Computer:
    def __init__(self, type, model, size):
        self.type = type
        self.model = model
        self.size = size
    def mobility(self):
        return False
class Laptop(Computer):
    def mobility(self):
        return True
class Personal_Computer(Computer):
    def mobility(self):
        return False
hp = Computer('computer', '15s', '3kg')
print(hp.mobility())

asus_flip = Laptop('laptop', '34d', '2.6kg')
print(asus_flip.mobility())