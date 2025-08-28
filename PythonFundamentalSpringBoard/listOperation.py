numbers = [1, 2, 3, 4, 5, 7, 43, [2, 44, 6, 7, 3, 2]]
letters = ['a', 'b', 'c', 'd', 'e', 'f']
# add lists
mix = letters + numbers
letters += numbers
print(mix)
print(letters)
print(letters[13][2])