#Write a program to show the use of different functions used in String
str1='prakash'
print(str1.capitalize())#capitalize: capitalize 1st letter as capital
print(str1.casefold())#casefold : makes all the letters into small case
print(str1.center(11))#center : create same ammount of spaces around string
print(str1.count('a'))#count : count number of occurances of a letter or string in a string
print(str1.encode())#encode : encodes the string
print(str1.endswith('sh'))#endswith : checks whether a string is ends with a perticular substring
str2='pra\tka\tsh'
print(str2.expandtabs(3))#expandtabs : increases tab number as per the input at the perviously tab location
print(str1.find('k'))#Searches the main string from the left for a specified substr
                    # ing and returns its position within a match is found; if not, return -1 when no match is found
print(str1.index('s'))#finds the occurance of a substring in a string and returns it's index
print(str1.isalnum())# checks if all the characters in a given string are alphanumeric or not
print(str1.isalpha())# checks if all the characters in a given string are alphabet or not
print(str1.isdecimal())# checks if all the characters in a given string are decimal or not
print(str1.isidentifier())# checks whether a string is a valid identifier or not
print(str1.islower())# checks whether all the characters in a string are in lower case or not
print(str1.isnumeric())# checks whether all the characters in a string are numeric or not
print(str1.isprintable())# checks whether all the characters in a string are printable or not
print(str1.isspace())# checks if all the characters in a string are white spaces or not
print(str1.istitle())# checks  if a string follows a set of rules to qualify as a title
print(str1.isupper())# Determines if all the characters in a given string are in the upper case
print(str1.join(str2))#Meant to concatenate two strings in an iterated manner
str3='PRAKASH'
print(str3.lower())#Meant to convert the entire string to lower case
print(str3.lower().upper())#Meant to convert the entire string to the upper case
print(str3.replace('PRA','pra'))#Meant to replace a substring with another