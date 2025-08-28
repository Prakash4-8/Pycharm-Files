# Selection sort program
arr = []
num = int(input('Enter size of the array : '))
for i in range(0, num):
    element = int(input('Enter number {} : '.format(i + 1)))
    arr.append(element)
print('Unsorted array : ', *arr)
for i in range(len(arr)):
    min = i
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[min]:
            min = j
    if min != arr[i]:
        arr[i], arr[min] = arr[min], arr[i]
print('After applying Selection Sort : ', *arr)