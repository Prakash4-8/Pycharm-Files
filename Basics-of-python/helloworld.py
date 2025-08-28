# print("THIS CODE IS WRITTEN IN PYCHARM  ")
# X=10
# Y=6575
# Z=X+Y
# print(Z)
#
class Student:
    def __init__(self,name,rollno):
        self.name =name
        self.rollno=rollno
        self.lap=self.Laptop()
    def show(self):
        print(self.name,self.rollno)
        self.lap.show()
    class Laptop:
        def __init__(self):
            self.brand='hp'
            self.cpu='i3'
            self.ram=8
        def show(self):
            print(self.brand,self.cpu,self.ram)
s1=Student('prakash',2)
s2=Student('siddharth',3)
s1.show()
lap1=s1.lap
lap2=s2.lap
