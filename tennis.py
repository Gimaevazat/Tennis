from graph import *
import random

def Key(event):
    pass
    #обработчик удержания клавиш влево, вправо, при которых ракетка 2 будет двигаться вправо, влево

def Mover1():
    pass
    #движение ракетки 1, ей управляет комп

def Mover2():
    pass
    #движение ракетки 2, управляет человвек

def Moveball():
    pass
    #движения шарика с ударом об стены и ракетки



Vball = 0
Vracket = 0



penSize(0)
brushColor(randColor())
rectangle(1, 1, 401, 601)
windowSize(402, 602)

brushColor(randColor())
racket1 = rectangle(20, 30, 80, 37)
racket2 = rectangle(20, 563, 80, 570)


brushColor(randColor())
ball = circle(200, 300, 5)

run()