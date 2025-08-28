#3. WAP to print all the prime numbers between given intervals as input from the user.
#For example Input- Starting interval-  2 , Ending interval- 10, Output- 2, 3, 5, 7 (Including the intervals)
start=int(input('Starting interval'))
end=int(input('Ending interval'))
for i in range(start,end+1):
        num=i
        if num== -1:
            break
        flag=True
        if num == 1 or num == 0:
            flag=False
        elif num > 1:
            for j in range(2,(num+2)//2):
                if num % j ==0:
                    flag=False
        if flag:
            print(i,end=',')
print('\b')
