import urwid
import numpy as np
import cletris_core
import time
import random

#TODO
"""
*) write a parser that colors based on number
*) rewrite the tetrominos to have individual numbers
*) rewrite the collisionfunction:
    a collision occurs when max(board + current) != max(board + next)
"""

#list of pieces
list_of_pieces = [cletris_core.i_bar(),
                  cletris_core.o_bar(),
                  cletris_core.l_bar(),
                  cletris_core.j_bar(),
                  cletris_core.s_bar(),
                  cletris_core.z_bar(),
                  cletris_core.t_bar()]
palette = [
    ('banner', '', '', '', '#ffa', '#60d'),
    ('streak', '', '', '', 'g50', '#60a'),
    ('inside', '', '', '', 'g38', '#808'),
    ('outside', '', '', '', 'g27', '#a06'),
    ('bg', '', '', '', 'g7', '#d06')]

#variables
a = 0
xax = 3
speed = 0.7
framerate = 0.01
# board
height = 17
width = 10
timestep = time.time()

board = np.zeros((height, width), dtype="int")



def update(key):    # key press handling
    global xax
    global piece

    if key in ("q", "Q"):
        raise urwid.ExitMainLoop()
    if key == "left":
        try:
            if xax>0:
                xax = xax-1
        except:
            pass
    if key == "right":
        try:
            if xax+piece.shape[1] < width:
                xax = xax+1
        except:
            pass
    if key in ("w", "W"):
        #TODO: improve l rotation
        try:
            if (xax+piece.shape[0]<=width) and (a+piece.shape[1]<=height) :
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

    try:
        if a<height:
            current = np.zeros((height, width), dtype="int")

            current[a:a+piece.shape[0], xax:xax+piece.shape[1]] = piece

            draw = str(board+current)
            draw = draw.replace("[", "")
            draw = draw.replace("]", "")
            #draw = draw.replace("0", " ")

            txt.set_text(f"{draw}")

            # increment y axis
            if time.time()-timestep>speed:

                #check if reached bottom or collision
                if ((a+1)+piece.shape[0] > height) or cletris_core.collision(board, cletris_core.move_down(current)):
                    board = board + current # add piece to background
                    piece = random.choice(list_of_pieces) #spawn a new piece
                    piece = piece.arr
                    xax = 3 # reset variables
                    a = 0
                else:
                    a = a+1

                timestep = time.time()
    except:
        pass
        #txt.set_text(f"{piece.shape[0]}")
        #raise urwid.ExitMainLoop()
        #txt.set_text(f"{a}")
    # run again in 0.5 seconds
    _loop.set_alarm_in(framerate, refresh)

#TODO: don't bind speed to framrate
loop.set_alarm_in(framerate, refresh)

loop.run()
