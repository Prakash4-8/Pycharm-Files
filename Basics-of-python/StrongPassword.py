#17. WAP to generate strong password of 8-alphanumerical.
# A password is said be strong if it has atleast one Lower case, one Upper case, one special character, and one number.
import random

capital = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
digit = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbol = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']
sum1 = capital + small + digit + symbol
rbigalpha = list(random.choice(capital))
rsmallalpha = list(random.choice(small))
rdigit = list(random.choice(digit))
rsymbol = list(random.choice(symbol))
sum2 = rsymbol + rdigit + rsmallalpha + rbigalpha + random.choices(sum1,k=4)
random.shuffle(sum2)
print(*sum2,sep='')
