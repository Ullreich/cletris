import urwid
import numpy
import time


def show_or_exit(key):
    if key in ("q", "Q"):
        raise urwid.ExitMainLoop()
    try:
        a = int(key)
        txt.set_text(("banner", f"the cube of {a} is {a**2}"))
    except:
        a = repr(key)
        #old_txt = txt.text
        txt.set_text(("banner", f"{str(key)} is not a number"))


palette = [
    ("banner", "black", "light gray"),
    ("streak", "black", "dark red"),
    ("bg", "black", "dark blue")]

txt = urwid.Text(("banner", f"{time.time()}"), align="center")
map1 = urwid.AttrMap(txt, "streak")
fill = urwid.Filler(map1)
map2 = urwid.AttrMap(fill, "bg")
loop = urwid.MainLoop(map2, palette, unhandled_input=show_or_exit)

loop.run()
