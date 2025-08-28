# 3. WAP to print all the words and the number of words in a sentence (String).
# Input: We are learning python is good speed
# Output (no force, you can print in any way you want):
# There are 7 words. They are 'We' 'are' 'learning' 'python' 'is' 'good' 'speed'
senten = input('Enter a sentence : ')
list1 = senten.split()
list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)
print('There are {} words. They are'.format(len(list2)),*list2,sep=",")