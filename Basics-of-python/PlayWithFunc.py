# Write a program to show DataType conversion of following (in single program)
#      int(), float(), str(), tuple(), list(), set(), dict(), chr(), hex(), oct()
x= input('Enter some value')
print('Float of {0} is {1}'.format(x,float(x)))
print('Integer of {0} is {1}'.format(x,int(x)))
char = ['p','r','a','k','a','s','h']
print('String of {0} is {1}'.format(char,str(char)))
print('Tuple of {0} is {1} '.format(x,tuple(x)))
print('List of {0} is {1} '.format(x,list(x)))
print('Set of {0} is {1} '.format(x,set(x)))
dict1={'roll1':'Siddharth','roll2':'prakash'}
print('Dictionary of {0} is {1} '.format(dict1,dict1['roll1']))
char2=99
print('Character of {0} is {1} '.format(char2,chr(char2)))
hexa=12
print('Hexadecimal of {0} is {1}'.format(hexa,hex(hexa)))
print('Octal of {0} is {1} '.format(hexa,oct(hexa)))