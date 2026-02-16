import turtle
import random
punts = 5

r = random.Random()

wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(600, 600)

t = turtle.Turtle()
t.shape("turtle")
t.color("green")
t.speed(punts)
t.penup()

msg_punts = turtle.Turtle()
msg_punts.ht()
msg_punts.color("white")
msg_punts.penup()

def tp_msg_punts(x, y):
    msg_punts.penup()
    msg_punts.goto(x, y)
    msg_punts.pendown()
def tp_tortuga(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def quadrat():
    t.goto(-200, 200)
    t.pendown()
    for _ in range(4):
        t.forward(400)
        t.right(90)
    t.penup()

def reapareixer_tortuga():
    coord_x = r.randrange(-180, 180)
    coord_y = r.randrange(-180, 180)
    tp_tortuga(coord_x, coord_y)

def tp_msg_punts(x, y):
    msg_punts.penup()
    msg_punts.goto(x, y)
    msg_punts.pendown()

def actualitzar_punts():
    msg_punts.clear()
    msg_punts.write(f"{punts}punts", align="center", font=("Arial", 30, "bold"))

def click(x, y):
    if t.distance(x, y) < 15:
        global punts
        punts += 1
        actualitzar_punts()
        reapareixer_tortuga()

tp_msg_punts(0, 250)
quadrat()
actualitzar_punts()

wn.listen()
wn.onscreenclick(click)
wn.onkeypress(wn.bye, "Escape")
wn.mainloop()