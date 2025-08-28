# 4. WAP to print the number of digits, lower case, upper case, spaces, special characters present in a given string.
# Input: aBc12 v$%Fq
# Output:
# number of digits- 2
# number of lower case- 4
# number of upper case- 2
# number of spaces - 1
# number of special characters- 2
stng =input('Enter a string : ')
lower = 0
digit = 0
upper = 0
space = 0
spechar = 0
for i in stng:
    if i.islower():
        lower+=1
    elif i.isdigit():
        digit+=1
    elif i.isupper():
        upper+=1
    elif i.isspace():
        space+=1
    else:
        spechar+=1
print('Number of digits {}\nNumber of lowercase letter {}\nNumber of uppercase letter {}\nNumber of spaces {}\nNumber of special characters {}'.format(digit,lower,upper,space,spechar))