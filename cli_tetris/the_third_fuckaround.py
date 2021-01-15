import numpy as np


def find_first_nonzero_right(tet):
    max = 0
    for row in tet[:]:
        for i in range(len(row)):
            if (row[i] != 0) and (i > max):
                max = i
    return max

def find_first_nonzero_down(tet):
    return find_first_nonzero_right(np.rot90(tet))

arr = np.array([[0, 5, 0],
                [0, 5, 5],
                [0, 0, 0]])

print(find_first_nonzero_down(arr))
