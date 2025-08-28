from collections import OrderedDict

a = OrderedDict(name='prakash', role='student', home='odisha')
c = OrderedDict(name='prakash', home='odisha', role='student')

print(a)
b = {}
dictionary_functions = dir(b)
OrderedDict_functions = dir(a)
print(dictionary_functions)

for i in OrderedDict_functions:
    if i not in dictionary_functions:
        print(i)

print(a == c)

d = {'name': 'prakash', 'role': 'student', 'home': 'odisha'}
e = {'name': 'prakash', 'home': 'odisha', 'role': 'student'}

print(d == e)
