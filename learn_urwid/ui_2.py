import urwid
import numpy as np

x = 0
y = 0
arr = np.zeros((16, 10), dtype = "int")


def update(key):
    if key in ("q", "Q"):
        raise urwid.ExitMainLoop()
    try:
        global x
        global y
        arr[x, y] = float(key)
        x = (x+1)%16
        if x==0:
            y = (y+1)%10
        str_array = str(arr)
        str_array = str_array.replace("[", "")
        str_array = str_array.replace("]", "")
        txt.set_text(f"{str_array}")
    except:
        pass

str_array = str(arr)
str_array = str_array.replace("[", "")
str_array = str_array.replace("]", "")
txt = urwid.Text(f"{str_array}", align="center")
fill = urwid.Filler(txt)
loop = urwid.MainLoop(fill, unhandled_input=update)

loop.run()
