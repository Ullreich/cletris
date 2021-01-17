import numpy as np

def update_highscore(score):
    # open the file. make it if it doesn't exist
    try:
        open("highscore.txt", "x")
    except:
        pass
    f = open("highscore.txt", "r")

    # turn file into list
    a = list()
    for i in f:
        a.append(int(i))

    #add score to scoreboard
    if (len(a) < 10):
        a.append(score)
    if score > min(a):
        a[9] = score

    a.sort(reverse = True)

    #write scores
    f = open("highscore.txt", "w")
    for i in a:
        f.write(f"{i}\n")
    f.close()

    return a

f = open("highscore.txt", "r")
stuff = f.read()

print(stuff)
