import numpy as np

height = 18
width = 12

board = np.zeros((height, width))
board[0:height, 0] = 9
board[0:height, width-1] = 9
board[height-1, 0:width] = 9

def collision(board, draw):
    for idx, i in np.ndenumerate(draw):
        if (i != 0) and (board[idx] != 0):
            return True
    return False

def clear_line(r):
    how_many = 0
    for i in range(r.shape[0]):
        if 0 not in r[i]:
            r = (np.concatenate((np.zeros((1, r.shape[1])), r[:i], r[i+1:])))
            how_many = how_many+1
    r = r.astype("int")
    return r, how_many

def color_board(tmp, width, color_black = False):
    colored_array = list()
    sleep = False
    #check for full lines
    if color_black:
        for i, j in zip(tmp, range(tmp.shape[0])):
            if 0 not in i:
                tmp[j] = [9 for k in range(tmp.shape[1])]

    #color array
    for idx, i in np.ndenumerate(tmp):
        if i == 1:
            colored_array.append(("l_blue", f" {i}"))
        elif i == 2:
            colored_array.append(("purple", f" {i}"))
        elif i == 3:
            colored_array.append(("yellow", f" {i}"))
        elif i == 4:
            colored_array.append(("blue", f" {i}"))
        elif i == 5:
            colored_array.append(("orange", f" {i}"))
        elif i == 6:
            colored_array.append(("red", f" {i}"))
        elif i == 7:
            colored_array.append(("green", f" {i}"))
        elif i == 9:
            colored_array.append(("black", f" {i}"))
        elif i == 0 and idx[1]%2==0:
            colored_array.append(("lavender", f" {i}"))
        else:
            colored_array.append(("snow", f" {i}"))

        if idx[1] == width-1:
            colored_array.append(f"\n")

    return colored_array


def move_down(arr):
    return np.concatenate(([arr[-1, :]], arr[:-1, :]))

def move_left(arr):
    return np.concatenate((arr[:, 1:], np.rot90([arr[:, 0]], axes=(1, 0))), axis=1)

def move_right(arr):
    return np.concatenate((np.rot90([arr[:, -1]], axes=(1, 0)), arr[:, :-1]), axis=1)

def find_first_nonzero_left(tet):
    min = 3
    for row in tet[:]:
        for i in range(len(row)):
            if (row[i] != 0) and (i < min):
                min = i
    return min

def find_first_nonzero_right(tet):
    max = 0
    for row in tet[:]:
        for i in range(len(row)):
            if (row[i] != 0) and (i > max):
                max = i
    return max

def find_first_nonzero_down(tet):
    return find_first_nonzero_right(np.rot90(tet))



class tetromino():
    arr = None
    color = None


class i_bar(tetromino):
    arr = np.array([[0, 0, 1, 0],
                    [0, 0, 1, 0],
                    [0, 0, 1, 0],
                    [0, 0, 1, 0]])

class t_bar(tetromino):
    arr = np.array([[0, 2, 0],
                    [2, 2, 0],
                    [0, 2, 0]])

class o_bar(tetromino):
    arr = np.array([[3, 3],
                    [3, 3]])

class j_bar(tetromino):
    arr = np.array([[0, 4, 0],
                    [0, 4, 0],
                    [4, 4, 0]])

class l_bar(tetromino):
    arr = np.array([[0, 5, 0],
                    [0, 5, 0],
                    [0, 5, 5]])

class z_bar(tetromino):
    arr = np.array([[0, 6, 0],
                    [6, 6, 0],
                    [6, 0, 0]])

class s_bar(tetromino):
    arr = np.array([[0, 7, 0],
                    [0, 7, 7],
                    [0, 0, 7]])

if __name__=="__main__":
    a = s_bar().arr
    print(a)
