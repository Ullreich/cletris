import urwid
import numpy as np
import cletris_core
import time
import random

#TODO
"""
implement line delete   [x]
implement topout        [x]
implement pause         [x]
implement speed drop    [x]
improve rotation        [ ]
research boxes          [x]
add nice kill screen    [ ]
    and reset option
implement preview       [x]
implement score         [x]
implement line count    [x]
    and speed up
implement high score    [ ]
    table
add music?              [ ]
pretty line deletion    [x]
clean up global with    [ ]
    classes?
update Colors           [ ]

clean up code
    4 important parts
        1) timing
        2) input
        3) game logic
        4) screen

fix:
when you rotate at the bottom or too far left the game crashes
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
    ("orange", "", "", "", "#f80", "#f80"),
    ("snow", "", "", "", "#AED", "#AED"),
    ("lavender", "", "", "", "#ACC", "#ACC")]

#variables
a = 0
xax = 4
speed = 0.5#0.7
level = 1
framerate = 0.001
height = 17
width = 10
timestep = time.time()
score = 0
lines = 0
next_piece = random.choice(list_of_pieces).arr
piece = random.choice(list_of_pieces).arr
pause_flag = False
down_speed = False

board = np.zeros((height, width), dtype="int")
current = None


def update(key):    # key press handling
    global xax
    global piece
    global pause_flag
    global down_speed

    if key in ("q", "Q"):
        raise urwid.ExitMainLoop()
    if key == "left":
        if xax+cletris_core.find_first_nonzero_left(piece)>0: #check if in bounds
            if not cletris_core.collision(board, cletris_core.move_left(current)): #check for collision
                xax = xax-1
    if key == "right":
        if xax+cletris_core.find_first_nonzero_right(piece)+1<width:
        #if xax+piece.shape[1] < width: #check if in bounds
            if not cletris_core.collision(board, cletris_core.move_right(current)):
                xax = xax+1
    if key in ("r", "R"):
        #TODO: improve l rotation
        if (xax+piece.shape[0]-1 < width): #make sure rotation is legal

            tmp_rot = np.zeros((height, width), dtype="int")
            tmp_piece = np.rot90(piece)
            tmp_rot[a:a+tmp_piece.shape[0], xax:xax+tmp_piece.shape[1]] = tmp_piece

            if not cletris_core.collision(board, tmp_rot): #make sure not to rotate into a piece
                piece = np.rot90(piece)
    if key in ("p", "P"):
        pause_flag = not pause_flag
    if key == "down":
        down_speed = True

#--------
#ui stuff
#--------

txt = urwid.Text((f"init"), align = "right") #main board

txt_next_piece = urwid.Text((f"init"), align = "left")  # next piece display
txt_next_padded = urwid.Padding(txt_next_piece, left = 4)

txt_meta = urwid.Text((f"Score:\n{score}\nLines:\n{lines}\nLevel:\n{level}"), align = "left")
txt_meta_padded = urwid.Padding(txt_meta, left = 4)

txt_next_piece_and_meta = urwid.Pile([txt_next_padded, txt_meta_padded])

full_board = urwid.Columns([txt, txt_next_piece_and_meta])
fill = urwid.Filler(full_board)
loop = urwid.MainLoop(fill, palette, unhandled_input=update)
loop.screen.set_terminal_properties(colors=256)

#-------------------
#refresh main screen
#-------------------

def refresh(_loop, _data):
    global board
    global a
    global xax
    global timestep
    global piece
    global next_piece
    global current
    global score
    global lines
    global level
    global speed
    global down_speed
    current_score = 0

    #check if game is paused
    if pause_flag == True:
        time.sleep(0.01)
        _loop.set_alarm_in(framerate, refresh)

    else:
        #draw the next piece
        filler = np.zeros((4, 4))
        filler[0:next_piece.shape[0], 0:next_piece.shape[1]] = next_piece
        filler = filler.astype("int")
        filler = cletris_core.color_board(filler, 4)
        txt_next_piece.set_text(([f"Next Piece:\n", filler]))

        #clear lines, increment score and line number, sleep on cleared line
        board, how_many = cletris_core.clear_line(board)
        if how_many != 0:
            time.sleep(speed*2)
            if lines >= 20*level:
                level = level + 1
                speed = speed* 2/3
            score = score + (how_many**2)*100*level
            lines = lines+how_many

        txt_meta.set_text(f"Score:\n{score}\nLines:\n{lines}\nLevel:\n{level}")

        #draw piece
        current = np.zeros((height, width), dtype="int")
        #current[a:a+piece.shape[0], xax:xax+piece.shape[1]] = piece[cletris_core.find_first_nonzero_in_row(piece):]
        for i, j in np.ndenumerate(piece):
            if j != 0:
                current[a+i[0], xax+i[1]] = j

        #check for collision:
        if cletris_core.collision(board, current):
            end_game = True
        else:
            end_game = False

        # add color:
        tmp = board + current
        if ((a+1)+piece.shape[0] > height) or cletris_core.collision(board, cletris_core.move_down(current)): #only color line black before new piece
            colored_array = cletris_core.color_board(tmp, width, True)
        else:
            colored_array = cletris_core.color_board(tmp, width)
        txt.set_text(colored_array)

        # increment y axis
        if down_speed:
            inc_speed = 0.01
            down_speed = False
        else:
            inc_speed = speed
        if time.time()-timestep>inc_speed:

            #check if reached bottom or collision
            if ((a+1)+cletris_core.find_first_nonzero_down(piece)+1 > height) or cletris_core.collision(board, cletris_core.move_down(current)):
                board = board + current # add piece to background

                #increment piece
                piece = next_piece

                #pick next piece
                next_piece = random.choice(list_of_pieces).arr #spawn a new piece

                # reset variables
                xax = 4
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
