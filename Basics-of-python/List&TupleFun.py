#Write a program to show the use of built-in methods used in List and Tuples
#------list function-------
list1=['p','r','a','k','a','s','h']
list1.append('m')# add an element at the end of a list
print(list1)
list1.clear()# clear all the elements in a list
print(list1)
list1.append('p')
list2=list1.copy()# copy all the elements of a list
print(list2)
occ=list1.count('d') # finds the number of times the element is present in the list
print(occ)
list1.extend(list2)#add elements of a list to the end of another list
print(list1)
list1.append('d')
print(list1.index('d'))#returns index of 1st element with specified value
list3=['m','o','h','a','p','a','t','a']
list3.insert(7,'r')# insert an element in a specified position
print(list3)
list3.pop(7)#removes an element from a specified position
print(list3)
list3.remove('a')#removes only first occurance an element from the list
print(list3)
list3.reverse()# reverce the order of a list
print(list3)
list3.sort()
print(list3)# sorts the list
#------tuple function-------
tuple1=(1,2,3,4,5,6,7,6)
print(tuple1.count(6))#count the frequency of an element
print(tuple1.index(6))# Search for the first occurrence of an element, and return its position
