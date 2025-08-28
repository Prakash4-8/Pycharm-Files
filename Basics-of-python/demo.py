# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
d = deque()
n_op = int(input())
for i in range(n_op):
    op_list = input().split(' ')
    if op_list[0] == 'append':
        d.append(op_list[1])
    elif op_list[0] == 'appendleft':
        d.appendleft(op_list[1])
    elif op_list[0] == 'pop':
        d.pop()
    elif op_list[0] == 'clear':
        d.clear()
    elif op_list[0] == 'extend':
        d.extend(op_list[1])
    elif op_list[0] == 'extendleft':
        d.extendleft(op_list[1])
    elif op_list[0] == 'count':
        d.count(op_list[1])
    elif op_list[0] == 'remove':
        d.remove(op_list[1])
    elif op_list[0] == 'reverse':
        d.reverse()
    elif op_list[0] == 'rotate':
        d.rotate(op_list[1])
print(d)
     
