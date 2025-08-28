# 4. WAP to print the smallest word present in the line of text (String). For example,
# Input- My name was Siddharth
# Output- My
def small(str):
    handle = str.split()
    small = 0
    for i in range(1,len(handle)):
        if len(handle[i]) < len(handle[small]):
            small = i
    return handle[small]
sen = input('Enter a sentence : ')
print('The smallest word is ',small(sen))