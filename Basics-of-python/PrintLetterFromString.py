"""9. WAP to print your name character by character. The output should be like this:
     For example
     INPUT: Python
     OUTPUT: P, y, t, h, o, n
    *Your output might have an extra "," after n. Your output|; P, y, t, h, o, n, (wrong output, remove the ",")"""
name=input('Enter name :')
for i in name:
    print(i,end=',')
print('\b')