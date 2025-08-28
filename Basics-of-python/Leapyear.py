#leap year program
x=int(input('Enter the year :'))
def Leapyear(z):
    con = False
    if z % 400 ==0:
        con=True
    elif z % 4 ==0 and z % 100 !=0 :
        con =True
    return con

if Leapyear(x) == True:
    print('This is a leap year')
else:
    print('This is not a leap year ')































