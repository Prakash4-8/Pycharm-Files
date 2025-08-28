#4. WAP to remove repeated numbers in a list. Print the list with unique value.
# For example Input- [5, 7, 5, 3, 2, 2, 1, 9, 2, 9,] Output: [5, 7, 3, 2, 1, 9]
list1=[]
num=int(input('Enter length of the list : '))
for i in range(0,num):
    list1.append(input('Enter element {} : '.format(i+1)))
print('Original list is : ',list1)
print('New list is : ',list(set(list1)))#using set function
print('Original list is : ',list1)
list2=[]
list3=list1
for i in list1:     # using not in
    if i not in list2:
        list2.append(i)
print('New list is :',list2)