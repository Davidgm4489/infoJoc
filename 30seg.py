import turtle
import random

punts = 0
temps = 10
record = 0
temporizador_actiu = False

r = random.Random()

wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(600, 600)

t = turtle.Turtle()
t.shape("turtle")
t.color("green")
t.pencolor("white")
t.speed(0)
t.penup()

msg_punts = turtle.Turtle()
msg_punts.ht()
msg_punts.color("white")
msg_punts.penup()

msg_temps = turtle.Turtle()
msg_temps.ht()
msg_temps.color("white")
msg_temps.penup()

def tp_tortuga(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
def tp_msg_punts(x, y):
    msg_punts.penup()
    msg_punts.goto(x, y)
    msg_punts.pendown()
def tp_msg_temps(x, y):
    msg_temps.penup()
    msg_temps.goto(x, y)
    msg_temps.pendown()

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

def actualitzar_punts():
    msg_punts.clear()
    msg_punts.write(f"Score: {punts}", align="center", font=("Arial", 30, "bold"))

def click(x, y):
    global punts
    if temps > 0:
        if t.distance(x, y) < 15:
            punts += 1
            actualitzar_punts()
            reapareixer_tortuga()

def temporitzador():
    global temps, record, temporizador_actiu
    if not temporizador_actiu:
        return
    msg_temps.clear()
    msg_temps.write(f"Time: {temps}", align="center", font=("Arial", 18, "bold"))
    if temps > 0:
        temps -= 1
        reapareixer_tortuga()
        wn.ontimer(temporitzador, 1000)
    else:
        temporizador_actiu = False
        msg_punts.clear()
        msg_temps.clear()
        tp_msg_punts(0, -20)
        msg_punts.write(f"Score: {punts}", align="center", font=("Arial", 40, "bold"))
        tp_msg_punts(0, 250)
        if punts > record:
            record = punts
            tp_msg_temps(0, 230)
            msg_temps.color("red")
            msg_temps.write("New record!!!", align="center", font=("Arial", 30, "bold"))
            msg_temps.color("white")
        tp_msg_temps(0, -200)
        msg_temps.write("Press R to restart", align="center", font=("Arial", 18, "bold"))
        tp_msg_temps(0, 210)

def reiniciar():
    global punts, temps, temporizador_actiu
    punts = 0
    temps = 10
    temporizador_actiu = True
    msg_punts.clear()
    msg_temps.clear()
    tp_msg_punts(0, 250)
    tp_msg_temps(0, 210)
    actualitzar_punts()
    reapareixer_tortuga()
    temporitzador()


tp_msg_punts(0, 250)
tp_msg_temps(0, 210)
quadrat()
actualitzar_punts()
reapareixer_tortuga()

temporizador_actiu = True
temporitzador()

wn.listen()
wn.onscreenclick(click)
wn.onkeypress(wn.bye, "Escape")
wn.onkeypress(reiniciar, "r")
wn.mainloop()