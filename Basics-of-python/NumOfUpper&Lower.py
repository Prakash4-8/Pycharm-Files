# 5. WAP to print the number of vowels and consonants in a string [focus on upper case & lower case].
# Input: PythonIsFun
# Output:
# Number of vowels - 3
# Number of consonants - 9
stng =input('Enter a string : ')
vowel =0
cons = 0
for i in stng:
    if i.isalpha():
        if i in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            vowel += 1
        else:
            cons += 1
print('Number of Vowels {}\nNumber of Consonants {}'.format(vowel,cons))