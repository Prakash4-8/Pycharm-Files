# Binary Search
list1 = [35, 44, 64, 65, 95]
find = int(input('Enter the number you want to search : '))
def BinarySearch(find, list, max, min):
    if max >= min:
        mid = (min + max)//2
        if find == list1[mid]:
            return mid
        elif find < list1[mid]:
            return BinarySearch(find, list, max -1, min)
        elif find > list1[mid]:
            return BinarySearch(find, list, max, min + 1)

x = BinarySearch(find, list1, len(list1) -1, 0)
if x == None:
    print('Element not found in the list !')
elif x >= 0:
    print('Element is present at index {}'.format(x))