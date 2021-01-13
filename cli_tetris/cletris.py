import urwid
import numpy as np
import cletris_core
import time
import random

#TODO
"""
implement line delete   [x]
implement topout        [x]
implement pause         [ ]
implement speed drop    [ ]
improve rotation        [ ]
research boxes          [ ]
add nice kill screen    [ ]
    and reset option
implement preview       [ ]
implement score         [ ]
implement line count    [ ]
    and speed up
implement high score    [ ]
    table
add music?              [ ]
pretty line deletion    [ ]
clean up global with    [ ]
    classes?

clean up code
    4 important parts
        1) timing
        2) input
        3) game logic
        4) screen
"""

#list of pieces
list_of_pieces = [cletris_core.i_bar(),
                  cletris_core.o_bar(),
                  cletris_core.l_bar(),
                  cletris_core.j_bar(),
                  cletris_core.s_bar(),
                  cletris_core.z_bar(),
                  cletris_core.t_bar()]

# TODO: fix palette
palette = [
    ('l_blue', '', '', '', '#0df', '#0df'),
    ("white", "", "", "", "#000", "#fff"),
    ("black", "", "", "", "#000", "#000"),
    ("yellow", "", "", "", "#ff0", "#ff0"),
    ("purple", "", "", "", "#808", "#808"),
    ("green", "", "", "", "#0d0", "#0d0"),
    ("red", "", "", "", "#f00", "#f00"),
    ("blue", "", "", "", "#00f", "#00f"),
    ("orange", "", "", "", "#f80", "#f80")]

#variables
a = 0
xax = 4
speed = 0.12#0.7
framerate = 0.001
height = 17
width = 10
timestep = time.time()
score = 0
lines = 0

board = np.zeros((height, width), dtype="int")
current = None



def update(key):    # key press handling
    global xax
    global piece

    if key in ("q", "Q"):
        raise urwid.ExitMainLoop()
    if key == "left":
        try:
            if xax>0: #check if in bounds
                if not cletris_core.collision(board, cletris_core.move_left(current)): #check for collision
                    xax = xax-1
        except:
            pass
    if key == "right":
        try:
            if xax+piece.shape[1] < width: #check if in bounds
                if not cletris_core.collision(board, cletris_core.move_right(current)):
                    xax = xax+1
        except:
            pass
    if key in ("w", "W"):
        #TODO: improve l rotation
        # fix collision on rotation
        try:
            if (xax+piece.shape[0]-1 < width): #make sure rotation is legal

                tmp_rot = np.zeros((height, width), dtype="int")
                tmp_piece = np.rot90(piece)
                tmp_rot[a:a+tmp_piece.shape[0], xax:xax+tmp_piece.shape[1]] = tmp_piece

                if not cletris_core.collision(board, tmp_rot): #make sure not to rotate into a piece
                    piece = np.rot90(piece)
        except:
            pass

#ui stuff
str_array = str(board)
str_array = str_array.replace("[", "")
str_array = str_array.replace("]", "")
#str_array = str_array.replace("0", " ")
txt = urwid.Text((f"{str_array}"), align="center")
fill = urwid.Filler(txt)
loop = urwid.MainLoop(fill, palette, unhandled_input=update)
loop.screen.set_terminal_properties(colors=256)

# for testing purposes run a piece down

piece = random.choice(list_of_pieces)
piece = piece.arr

def refresh(_loop, _data):
    global board
    global a
    global xax
    global timestep
    global piece
    global current
    global score
    global lines
    current_score = 0

    board, how_many = cletris_core.clear_line(board)
    if how_many != 0:
        time.sleep(speed*2)
    score = score + (how_many**2)*100
    lines = lines+how_many

    #draw piece
    current = np.zeros((height, width), dtype="int")
    current[a:a+piece.shape[0], xax:xax+piece.shape[1]] = piece

    #check for collision:
    if cletris_core.collision(board, current):
        end_game = True
    else:
        end_game = False

    # add color:
    tmp = board + current

    colored_array = cletris_core.color_board(tmp, width, True)
    txt.set_text(colored_array)

    # increment y axis
    if time.time()-timestep>speed:

        #check if reached bottom or collision
        if ((a+1)+piece.shape[0] > height) or cletris_core.collision(board, cletris_core.move_down(current)):
            board = board + current # add piece to background

            piece = random.choice(list_of_pieces) #spawn a new piece
            piece = piece.arr
            xax = 4 # reset variables
            a = 0
        else:
            a = a+1

        timestep = time.time()

    # run again in framerate
    if end_game == False:
        _loop.set_alarm_in(framerate, refresh)
    else:
        txt.set_text(f"game over\n:(")

loop.set_alarm_in(framerate, refresh)

loop.run()
