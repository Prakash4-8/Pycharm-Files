# read pair of integer line by line
string_array=[]
def getdata():
    while True:
        value = input("Enter integer pair (hit Enter to quit)")
        if value == "":
            break
        string_array.append(value)
    print(string_array)

tuple_array=[]
# convert string to tuple
def extractValue():
 
    for i in string_array:
        tuple_val = tuple(i.split())
        tuple_array.append(tuple_val)
    print(tuple_array)

reslut_array=[]
# calculate the ratio of tuple
def calcRatios():
    for i in tuple_array:
        result = int(i[0])/int(i[1])
        reslut_array.append(result)
    print(reslut_array)


getdata()
extractValue()
calcRatios()
