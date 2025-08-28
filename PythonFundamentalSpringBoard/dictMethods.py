letters = ['a', 'b', 'c', 'd', 'e']
scores = {
    'Bob': 20,
    'Alice': 23,
    'jim': 22
}
"""
dict_name.update()
dictname.keys()
dict.fromkeys(list)
min()
max()

"""

a = {
    'Prakash': 34,
    'Vikash': 56
}
scores.update(a)
print(scores)
keys = scores.keys()
print(keys)

new_dict = dict.fromkeys(letters)
print(new_dict)

print(min(scores))
print(max(scores))

# require at least one argument
print(scores.pop('Prakash'))  # returning the value of the dictionary
print(scores)

print(scores.popitem())  # will return the total element of the dictionary
print(scores)

scores.clear()
print(scores)

