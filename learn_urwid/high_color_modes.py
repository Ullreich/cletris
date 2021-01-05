import urwid

def exit_on_q(key):
    if key in ("q", "Q"):
        raise urwid.ExitMainLoop()

palette = [
    ("banner", "", "", "", "#ffa", "#60d"),
    ("streak", "", "", "", "#ffb", "#60a"),
    ("inside", "", "", "", "#ff3", "#808"),
    ("outside", "", "", "", "#ff0", "#a06"),
    ("bg", "", "", "", "#fe8", "#d06")]

placeholder = urwid.SolidFill()
loop = urwid.MainLoop(placeholder, palette, unhandled_input=exit_on_q)
loop.screen.set_terminal_properties(colors=256)
loop.widget = urwid.AttrMap(placeholder, "bg")
loop.widget.original_widget = urwid.Filler(urwid.Pile([]))

div = urwid.Divider()
outside = urwid.AttrMap(div, "outside")
inside = urwid.AttrMap(div, "inside")
txt = urwid.Text(("banner", f"hello there"), align="center")
streak = urwid.AttrMap(txt, "streak")
pile = loop.widget.base_widget #base widget skips decorations
for item in [outside, inside, streak, inside, outside]:
    pile.contents.append((item, pile.options()))

loop.run()
