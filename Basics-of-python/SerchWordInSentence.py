# 7. WAP to search a word in a string, accepted by the user. If the word is present then print YES along with its position otherwise display an appropriate message. For example,
# Input- Python is good for AI.
# Search word- good
# Output- YES, the searched word is present at 11 positions. (10 index number)
# * Print as per your convenience *
sen = input('Enter a sentence : ')
word = input('Enter word you want to search :')
x = sen.find(word)
if x >= 0:
    print('Yes, the searched word is present at {} position'.format(x + 1))
else:
    print('No, the searched word is not present in the sentence')