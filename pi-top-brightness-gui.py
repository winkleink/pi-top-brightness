#!/usr/bin/env python3

# Small GUI program using GUIZero to change the 
# brightness of a Pi-top/CEED if using Jessie and not pi-topOS

# to use this program you first have to install the code from
# https://github.com/rricharz/pi-top-install
# to get the brightness command
# while there it's worth installing the shutdown code too
# as it will shutdown the pi-top hub when you shutdown Jessie

# as of the latest Jessie guizero is pre-installed so no other
# software should need to be installed.
# if guizero is not installed then follow these instruction
# https://lawsie.github.io/guizero/
# this program is python 3 and needs to be made executable with
# chmod +x pi-top-brightness-gui.py
# might be good to change the name of the program to something shorter

from guizero import *
from subprocess import call

def do_nothing():
    print("Nothing happened")
    
def brighter():
    call(["brightness", "increase"])

    
def darker():
    call(["brightness", "decrease"])
    
    
app = App(title="pi-top", height=50, width=145, layout="grid", bgcolor=None)

button1 = PushButton(app, brighter, text="Brighter", grid=[0,1])
button2 = PushButton(app, darker, text="Darker", grid=[0,0])
app.display()
