# Bubble Sort
list1 = [12, 24, 25, 89, 12, 37, 82, 45, -2, -5, 87, 82, 92, 99]
for j in range(len(list1) - 1):
    s = False
    for i in range(len(list1) - 1):
        if list1[i] > list1[i + 1]:
            list1[i + 1] = list1[i] + list1[i + 1]
            list1[i] = list1[i + 1] - list1[i]
            list1[i + 1] = list1[i + 1] - list1[i]
            s = True
    if s == False:
        break

print(list1)

