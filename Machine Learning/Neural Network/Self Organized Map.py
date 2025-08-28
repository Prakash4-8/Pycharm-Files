import numpy as np

# Initializations
# input Array
# i1 = np.array([1, 1,0,0]); i2 = np.array([0,0,0,1]);
# i3 = np.array([1, 0,0,0]);i4 = np.array([0, 0,1,1]); i_values = [i1, i2, i3, i4]

i_values = [np.array([1, 1, 0, 0]), np.array([0, 0, 0, 1]), np.array([1, 0, 0, 0]), np.array([0, 0, 1, 1])]

unit_1 = np.array([0.2, 0.6, 0.5, 0.9])
unit_2 = np.array([0.8, 0.4, 0.7, 0.3])

learning_rate = 0.6


def update(unit, iValues):
    return np.array(unit + learning_rate * (iValues - unit))


i_w = 0


def inner_loop(i_values, i):
    global unit_1, unit_2

    d_for_unit_1 = (unit_1[0] - i_values[i][0]) ** 2 + (unit_1[1] - i_values[i][1]) ** 2 + (
                unit_1[2] - i_values[i][2]) ** 2 + (unit_1[3] - i_values[i][3]) ** 2
    print('D1',d_for_unit_1)
    d_for_unit_2 = (unit_2[0] - i_values[i][0]) ** 2 + (unit_2[i] - i_values[i][1]) ** 2 + (
                unit_2[2] - i_values[i][2]) ** 2 + (unit_2[3] - i_values[i][3]) ** 2
    print('D2',d_for_unit_2)
    if d_for_unit_1 < d_for_unit_2:
        updated_unit_1 = update(unit_1, i_values[i])
        unit_1 = updated_unit_1
        updated_unit_2 = unit_2
        return 'unit_1'
    else:
        updated_unit_2 = update(unit_2, i_values[i])
        unit_2 = updated_unit_2
        updated_unit_1 = unit_1
        return 'unit_2'


print('Assuming iteration starts from iter = 1 for users.')
print('The iteration actually starts from 0 .')

prev_update_seq = []

for i in range(4):
    returned = inner_loop(i_values, i)
    prev_update_seq.append(returned)
iter = 0
while (True):
    curr_update_seq = []
    for i in range(4):
        returned = inner_loop(i_values, i)
        curr_update_seq.append(returned)
    flag = 0
    for i in range(len(curr_update_seq)):
        if (prev_update_seq[i]==curr_update_seq[i]):
            flag = 1
            break
    if flag == 1:
        print('Termination loop at iteration: ', iter + 2, 'No updates anymore.')
        break
        iter += 1

print('Final Sequence: ', curr_update_seq)

