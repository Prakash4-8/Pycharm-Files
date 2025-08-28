import Palindrome
# 1. Program to check whether each element in the 'list' are palindrome or not.
#
# For example:
# a) Input: que_list = ['madam', 1221, 'abcba', 'c', 9]
# Output: Yes, all the list's elements are palindrome
# b) Input: que_list = [' ',98589, 'Madamji' ]
# Output: No, list's elements aren't palindrome
lis1 = ['22322','aamaa','sus']
flg = True
for i in lis1:
    if Palindrome.palindrome(i) == False:
        flg = False
        break
if flg:
    print('All the list elements are palindrome')
else:
    print('List elements are not palindrome')
