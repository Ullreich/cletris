import numpy as np

height = 18
width = 12

board = np.zeros((height, width))
board[0:height, 0] = 9
board[0:height, width-1] = 9
board[height-1, 0:width] = 9

# print(board)

"""
def collision(board, draw):
    if 2 in board + draw:
        return True
    return False
"""

def collision(board, draw):
    for idx, i in np.ndenumerate(draw):
        if (i != 0) and (board[idx] != 0):
            return True
    return False


def move_down(arr):
    return np.concatenate(([arr[-1, :]], arr[:-1, :]))

def move_left(arr):
    return np.concatenate((arr[:, 1:], np.rot90([arr[:, 0]], axes=(1, 0))), axis=1)

def move_right(arr):
    return np.concatenate((np.rot90([arr[:, -1]], axes=(1, 0)), arr[:, :-1]), axis=1)


class tetromino():
    arr = None
    color = None


class i_bar(tetromino):
    arr = np.array([[1, 1, 1, 1]])

class t_bar(tetromino):
    arr = np.array([[0, 2],
                    [2, 2],
                    [0, 2]])

class o_bar(tetromino):
    arr = np.array([[3, 3],
                    [3, 3]])

class j_bar(tetromino):
    arr = np.array([[0, 4],
                    [0, 4],
                    [4, 4]])

class l_bar(tetromino):
    arr = np.array([[5, 0],
                    [5, 0],
                    [5, 5]])

class z_bar(tetromino):
    arr = np.array([[0, 6],
                    [6, 6],
                    [6, 0]])

class s_bar(tetromino):
    arr = np.array([[7, 0],
                    [7, 7],
                    [0, 7]])

if __name__=="__main__":
    a = s_bar().arr
    print(a)
