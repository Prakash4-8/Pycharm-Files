# 10. WAP to print the input word (String) in alphabetical order. For example,
# Input: sonali (ignore uppercase & lowercase conflict)
# Ouput- ailnos
#
# Input: madam
# Output: aadmm
word = input('Enter a word : ')
word2=sorted(word)
print('The sorted sequence is ',*word2,sep='')