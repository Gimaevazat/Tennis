from tkinter import *
from graph import *
import random
Score = 0
#Ракетка игрока
def Moveracket2(event):
    global x2, y2, racket2, Vracket
    if x2 < 340:
        if event.keycode == VK_RIGHT:
            x2 += Vracket
    if x2 > 2:
        if event.keycode == VK_LEFT:
            x2 -= Vracket
    moveObjectTo(racket2, x2, y2)
#Ракетка противника
def Moveracket1():
    global x1, y1, racket1
    if x1 < 340 and x1 < xball:
        x1 += Vracket
    if x1 > 2 and x1 + 60 > xball:
        x1 -= Vracket
    moveObjectTo(racket1, x1, y1)

# Теннисный мяч
def Moveball():
    global Vxball, Vyball, xball, yball, ball
    if xball > 385:
        Vxball = - Vxball
    if xball < 2:
        Vxball =  -Vxball
    if yball > y2 - 15 and xball > x2 - 8  and xball < x2 + 54:
        Vyball = -Vyball
    if yball < y1 + 9 and xball > x1 - 8  and xball < x2 + 54:
        Vyball = -Vyball
    if yball < 555:
        Score =+ 1
    if Score == 5:
        end()
    xball += Vxball
    yball += Vyball
    moveObjectTo(ball, xball, yball)

def end():
    pass
    # конец игры

Vxball = 5
Vyball  = 7
Vracket = 7
x2 = 20
y2 = 563
x1 = 20
y1 = 30
xball = 20
yball = 300
#Дизфйн стола
penSize(0)
brushColor("green")
rectangle(1, 1, 401, 601)
windowSize(402, 602)
#Дизайн ракеток
brushColor("red")
racket1 = rectangle(x1, y1, x1 + 60, y1 + 7)
brushColor("blue")
racket2 = rectangle(x2, y2, x2 + 60, y2 + 7 )

#Дизайн мяча
brushColor("orange")
ball = circle(xball, yball, 7)

onTimer(Moveball, 50)
onTimer(Moveracket1, 50)
onKey(Moveracket2)

run()