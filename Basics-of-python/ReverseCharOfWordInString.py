# 5. WAP to reverse each word in the string (line of text). For example,
# Input- This is python programming
# output- sihT si nohtyp gnimmargorp
sentence = input('Enter a sentence : ')
list1 = sentence.split()
fsen = ''
for i in list1:
    for j in range(len(i) - 1,-1,-1):
        print(i[j],end='')
    print('',end=' ')