import urwid
import numpy as np

def exit_on_q(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()

palette = [
    ('banner', 'black', 'light gray'),
    ('streak', 'black', 'dark red'),
    ('bg', 'black', 'dark blue')]

outo =  np.zeros((5, 5), dtype="int")
outo[3, 3] = 5

ini = []
for idx, i in np.ndenumerate(outo):
    if idx[1]==4:
        ini.append(f"\n")
    elif i != 0:
        ini.append(("streak", f" {i} "))
    else:
        ini.append(("banner", f" {i} "))

#txt = urwid.Text([('banner', u"start in attr1 "), ('streak', u"end in attr2")])
txt = urwid.Padding(urwid.Text(ini, wrap="space"), left=2, right=2, min_width=20)
map1 = urwid.AttrMap(txt, 'streak')
fill = urwid.Filler(map1)
map2 = urwid.AttrMap(fill, 'bg')
loop = urwid.MainLoop(map2, palette, unhandled_input=exit_on_q)




loop.run()

#print(ini)
