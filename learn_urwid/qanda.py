import urwid

def exit_on_q(key):
    if key in ("q", "Q"):
        raise urwid.ExitMainLoop()

class QuestionBox(urwid.Filler):
    def keypress(self, size, key):
        if key != "enter":
            return super(QuestionBox, self).keypress(size, key)
        self.original_widget = urwid.Text(
            ("text", f"nice to meet you\n{edit.edit_text}\nPress q to exit"),
            align="center"
        )

palette = [
    ("bg", "black", "dark red"),
    ("text", "black", "light green")]

edit = urwid.Edit(("text", f"what is your name?\n"), align="center")
fill = QuestionBox(edit)
map1 = urwid.AttrMap(fill, "bg")

loop = urwid.MainLoop(map1, palette, unhandled_input=exit_on_q)
loop.run()
