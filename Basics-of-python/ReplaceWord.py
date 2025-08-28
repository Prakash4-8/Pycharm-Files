# 8.WAP to replace a word with a searched word if found otherwise print "Can't replace because searched word not found".
# For example,
# Input- Python is good for AI
# Search word- good
# Replace word- best
# Output- Python is best for AI
sen = input('Enter a sentence : ')
list1 = sen.split()
word = input('Enter word you want to search :')
replace = input('Enter a word to replace :')

if word in list1:
    list1[list1.index(word)] = replace
    print(*list1,end=' ')
else:
    print('No, the searched word is not present in the sentence')