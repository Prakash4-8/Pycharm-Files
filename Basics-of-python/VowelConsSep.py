# 6. WAP to print vowels first, then consonants in a string.
# Ex: Input - PythonIsFun
# Output - oIuPythnsFn
name = input('Enter a string : ')
vow=''
cons=''
for i in name:
    if i.isalpha():
        if i in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            vow +=i
        else:
            cons += i
print(vow,cons,sep='')