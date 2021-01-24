# Cletris.py
a cli clone of the classic game Tetris written in python.<br>
Written in python 3.8, no guarantees it works in earlier versions. Will not
work in python 2.

![an example image of cletris](/example_image.png "i am not good at tetris :(")

## dependencies:
* numpy  (tested with version 1.19.2)
* urwid  (tested with version 2.1.2)

## install:
1. make sure the dependencies are installed (`pip3 install urwid numpy`)
2. clone this Repo (`git clone https://github.com/Ullreich/cletris`)
3. `cd` into the directory and run script with `python3 cletris.py`

<b>if you want to be able to execute cletris from anywhere:</b>
4. add this directory to your PATH in your `.bashrc` (or `.bash_profile` on mac)
5. set the file to be executable `chmod +x cletris.py`
6. run script with `cletris.py`

## controls:
* Q/q: quit
* R/r: rotate right
* P/p: pause/unpause
* left arrow: move tetromino left
* right arrow: move tetromino right
* down arrow: push tetromino down
