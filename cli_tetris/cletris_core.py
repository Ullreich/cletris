import numpy as np

height = 18
width = 12

board = np.zeros((height, width))
board[0:height, 0] = 9
board[0:height, width-1] = 9
board[height-1, 0:width] = 9

# print(board)


def collision(board, draw):
    if 2 in board + draw:
        return True
    return False

def move_down(arr):
    return np.concatenate(([arr[-1, :]], arr[:-1, :]))

class tetromino():
    arr = None
    color = None


class i_bar(tetromino):
    arr = np.array([[1, 1, 1, 1]])

class t_bar(tetromino):
    arr = np.array([[0, 1],
                    [1, 1],
                    [0, 1]])

class o_bar(tetromino):
    arr = np.array([[1, 1],
                    [1, 1]])

class j_bar(tetromino):
    arr = np.array([[0, 1],
                    [0, 1],
                    [1, 1]])

class l_bar(tetromino):
    arr = np.array([[1, 0],
                    [1, 0],
                    [1, 1]])

class z_bar(tetromino):
    arr = np.array([[0, 1],
                    [1, 1],
                    [1, 0]])

class s_bar(tetromino):
    arr = np.array([[1, 0],
                    [1, 1],
                    [0, 1]])

if __name__=="__main__":
    a = s_bar().arr
    print(a)
