import turtle
import random
contador = 5

r = random.Random()

wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(600, 600)

t = turtle.Turtle()
t.shape("turtle")
t.color("green")
t.speed(contador)
t.penup()

def actualitzar_pts():
    msg_pts.clear()
    msg_pts.write(f"{pts}pts", align="center", font=("Arial", 30, "bold"))

def click(x, y):
    if -150 < x < 150 and -150 < y < 150:
        global pts
        pts += multiplicador
        actualitzar_tot()

wn.listen()
wn.onscreenclick(click)
wn.onkeypress(wn.bye, "Escape")