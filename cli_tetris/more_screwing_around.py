import urwid
import numpy as np
#import cletris_core

rub = [["ferdi", 34],
     ["ferdi", 4545],
     ["rubus", 5]]

def update_highscore(score):
    #save('data.npy', data)
    try:
        hiscore = np.load("highscore.npy")
    except:
        open("highscore.npy", "x")

    if len(highscore) <= 10:
        highscore = np.concatenate((highscore, score))

    np.save("highscore.npy", highscore)


def exit_on_q(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()

class QuestionBox(urwid.Filler):
    def keypress(self, size, key):
        if key != 'enter':
            return super(QuestionBox, self).keypress(size, key)
        self.original_widget = urwid.Text((
            f"game over\n:(\nHighscore:\n{content}\n{edit.edit_text}"),
            align = "center")

#cletris_core.update_highscore(score)
#f = open("highscore.txt", "r")
#content = f.read()

#for i in rub:
update_highscore(rub[0])


"""
edit = urwid.Edit(f"congratulations, please enter name\n")
fill = QuestionBox(edit)
loop = urwid.MainLoop(fill, unhandled_input=exit_on_q)
loop.run()
"""
