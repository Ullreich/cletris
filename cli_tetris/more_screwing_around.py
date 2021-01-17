import urwid
import numpy as np
import time

def exit_on_q(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()


palette = [
    ('banner', 'black', 'light gray'),
    ('streak', 'black', 'dark red'),
    ('bg', 'black', 'dark blue')]

txt = urwid.Text("hallo")
fill = urwid.Filler(txt)
my_screen = urwid.raw_display.Screen()
loop = urwid.MainLoop(fill, screen=my_screen)


loop.start()
loop.draw_screen()
time.sleep(1)

new_txt = urwid.Text("goodbye")
try:
    my_screen.clear()
    fill = urwid.Filler(new_txt)
    #loop(fill)
    loop.draw_screen()
except:
    print("cock")
    pass
time.sleep(1)

loop.stop()
