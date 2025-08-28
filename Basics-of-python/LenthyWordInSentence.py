# 3. WAP to print the biggest word present in the line of text (string). For example,
# Input- My name is Siddharth
# Output- Siddharth
def lenthy(str):
    handle = str.split()
    big = 0
    for i in range(0,len(handle)):
        if len(handle[i]) > len(handle[big]):
            big = i
    return handle[big]
sen = input('Enter a sentence : ')
print('The biggest word is ',lenthy(sen))