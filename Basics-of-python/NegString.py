#10. WAP to show the use of negative indexes of string.
name = input('Enter name :')
for i in range(-len(name), 0):
    print(name[i])
