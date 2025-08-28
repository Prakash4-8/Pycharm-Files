#Write a program to show the use of built-in methods used in dictionary
dict1={'name':'prakash','cell num':'753787453','address':'bhagada,tesinga,bhandaripokhari,bhadral'}
dict2=dict1.copy()#used to copy a dictionary
dict1.clear()#used to clear all the elements of the dictionary
print(dict1)
dict1={'name','cell num','address'}
dict1=dict.fromkeys(dict1,'null')#Returns a dictionary with the specified keys and value#
print(dict1)
print(dict2.get('address'))#returns the value of a specified key
print(dict2.items())#Returns a list containing a tuple for each key value pair
print(dict2.keys())#Returns a list containing the dictionary's keys
dict2.pop('cell num')
print(dict2)
dict2.popitem()#Removes the last inserted key-value pair
print(dict2)
dict2.setdefault('pin','756121')#The setdefault() method returns the value of the item with the specified key.
print(dict2) #If the key does not exist, insert the key, with the specified value
dict2.update({'sex':'male'})# it is used to insert an element into dictionary
print(dict2)
print(dict2.values())# returns the values of the dictionary