a = {1, 2, 3}
b = {2, 3, 4, 5}
print(a)
for i in a:
    print(i)
a.add(4)
print(a)
a.update(b)
print(a)
a.remove(5)  # it will give error if value is not present in the set
print(a)
a.discard(8)  # it will not give error if the value is not present in the set
print(a)
print(a.pop()) # it will pop the 1st element of the set
