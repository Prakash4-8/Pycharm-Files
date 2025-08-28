#8. WAP to store the marks of N subjects of a student in a LIST and calculate the percentage, average, and grade/division.
# Take max mark is 100. Print Invalid Mark of user input more than 100.
num=int(input('Enter number of subjects :'))
student=[]
i=0
marksum=0
while num > i:
    mark = int(input('Enter mark {0} :'.format(i+1)))
    if mark <= 100:
        student.append(mark)
        marksum+=student[i]
        i+=1
    else:
        print('Invalid input')
percentage=marksum/i
print('Percentage is {0}%'.format(percentage))
print('Average is {0}'.format(percentage))
if percentage > 90:
    print('Grade is A++')
elif 80 < percentage <= 90:
    print('Grade is A')
elif 70 < percentage <= 80:
    print('Grade is B++')
elif 60 < percentage <= 70:
    print('Grade is B')
elif 50 < percentage <= 60:
    print("Grade is C++")
elif 40 < percentage <= 50:
    print('Grade is C')
else:
    print('Grade is F')