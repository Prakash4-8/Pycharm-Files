name = 'Prakash'
sub = 'ka'
for i in range(len(name) - len(sub)):
    j = 0
    while(j < len(sub)):
        if name[i + j] == sub[j]:
            j +=1
        else:
            break
    else:
        print('The position of sub-element in the full element is',i)