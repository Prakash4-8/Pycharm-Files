from faveObjects.carMeth import *
from faveObjects import browserClassMethod as wb
my_car = Car('Honda', '2.1', 2022, 1400, 220)
my_car.accleratre(5)
print(my_car.__dict__)
mozilla = wb.WebBrowser('Brave')
mozilla.navigate('instagram')
print(mozilla.__dict__)