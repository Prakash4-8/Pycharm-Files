#4. WAP (Write A Program) to print odd numbers or even numbers between 25 to 50 using a while loop. The output should be like this:
#     25 is an odd number
 #    26 is an even number
  #   ........
   #  50 is an even number
i=25
while i < 51:
    if i % 2 == 0:
        print(i,'is an even number')
    else:
        print(i,'is an odd number')
    i+=1