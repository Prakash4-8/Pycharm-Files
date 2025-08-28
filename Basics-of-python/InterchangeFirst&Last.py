# 2. WAP to accept a line of text (String) from the user and modify it such that the first word and the last word will be interchanged.
# For example Input- It doesn't make sense
# Output- sense doesn't make it
name = input('Enter a string : ')

def swaps(name):
    temp = name.split()
    print(temp[len(temp)-1],end=' ')
    for i in range(1,len(temp)-1):
        print(temp[i],end=' ')
    print(temp[0])
swaps(name)