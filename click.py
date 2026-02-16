import turtle
import random

pts = 2000
multiplicador = 1
preu_click = 100
preu_auto = 1000
clicks = 1
auto = 1

r = random.Random()
wn = turtle.Screen()
wn.setup(800, 600)
dibuix = turtle.Turtle()
dibuix.pencolor("black")
dibuix.speed(0)
dibuix.ht()

msg_pts = turtle.Turtle()
msg_pts.ht()
msg_pts.color("black")
msg_pts.penup()
msg_multipilicador = turtle.Turtle()
msg_multipilicador.ht()
msg_multipilicador.color("black")
msg_multipilicador.penup()
msg_preu = turtle.Turtle()
msg_preu.ht()
msg_preu.color("black")
msg_preu.penup()
msg_auto = turtle.Turtle()
msg_auto.ht()
msg_auto.color("black")
msg_auto.penup()

def tp_dibuix(x, y):
    dibuix.penup()
    dibuix.goto(x, y)
    dibuix.pendown()
def tp_msg_pts(x, y):
    msg_pts.penup()
    msg_pts.goto(x, y)
    msg_pts.pendown()
def tp_msg_multipilicador(x, y):
    msg_multipilicador.penup()
    msg_multipilicador.goto(x, y)
    msg_multipilicador.pendown()
def tp_msg_preu(x, y):
    msg_preu.penup()
    msg_preu.goto(x, y)
    msg_preu.pendown()
def tp_msg_auto(x, y):
    msg_auto.penup()
    msg_auto.goto(x, y)
    msg_auto.pendown()

def actualitzar_pts():
    msg_pts.clear()
    msg_pts.write(f"{pts}pts", align="center", font=("Arial", 30, "bold"))
def actualitzar_multipilicador():
    msg_multipilicador.clear()
    msg_multipilicador.write(f"x{multiplicador}", align="center", font=("Arial", 24, "bold"))
def actualitzar_preu():
    msg_preu.clear()
    msg_preu.write(f"x1: {preu_click}pts", align="center", font=("Arial", 18, "bold"))
def actualitzar_auto():
    msg_auto.clear()
    msg_auto.write(f"x1: {preu_auto}click/seg", align="center", font=("Arial", 18, "bold"))
def actualitzar_tot():
    actualitzar_pts()
    actualitzar_multipilicador()
    actualitzar_preu()
    actualitzar_auto()

def click(x, y):
    if -150 < x < 150 and -150 < y < 150:
        global pts
        pts += multiplicador
        actualitzar_tot()

def comprar_click():
    global multiplicador, pts, preu_click, clicks
    if pts >= preu_click:
        multiplicador += 1
        pts += -preu_click
        actualitzar_tot()
        preu_click = 100 + (2 * clicks) ** 2
        clicks += 1

def autoclicker():
    global pts, multiplicador, preu_auto, auto
    if pts >= preu_auto:
        pts += auto
        actualitzar_tot()
        auto += 1
        preu_auto = 1000 + (5 * auto) ** 2
        wn.ontimer(autoclicker, 1000)

tp_dibuix(-200, 200)
for _ in range(4):
    dibuix.forward(400)
    dibuix.right(90)
dibuix.penup()

dibuix.pencolor("blue")
dibuix.fillcolor("yellow")
tp_dibuix(0, -150)
dibuix.begin_fill()
dibuix.circle(150)
dibuix.end_fill()

tp_msg_pts(0, 0)
tp_msg_multipilicador(0, 250)
tp_msg_preu(300, 100)
tp_msg_auto(300, -100)

wn.listen()
wn.onscreenclick(click)
wn.onkeypress(wn.bye, "Escape")
wn.onkeypress(comprar_click, 1)
wn.onkeypress(autoclicker, 2)

actualitzar_tot()

wn.mainloop()