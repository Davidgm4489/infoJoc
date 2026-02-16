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

c = turtle.Turtle()
c.pencolor("yellow")
c.speed(0)
c.ht()

msg = turtle.Turtle()
msg.ht()
msg.color("white")
msg.penup()

wn.tracer(0)
t.goto(-150, 0)
msg.goto(0, 250)

def quadrat():
    t.goto(-200, 200)
    t.pendown()
    for _ in range(4):
        t.forward(400)
        t.right(90)
    t.penup()

def tp(x, y):
    t.penup()
    t.goto(x, y)

def tp_dibuix(x, y):
    c.penup()
    c.goto(x, y)
    c.pendown()

def up():
    t.sety(t.ycor() + contador)
    t.setheading(90)

def down():
    t.sety(t.ycor() - contador)
    t.setheading(-90)

def right():
    t.setx(t.xcor() + contador)
    t.setheading(0)

def left():
    t.setx(t.xcor() - contador)
    t.setheading(180)

def generar_moneda():
    global hit_x, hit_y
    
    c.clear()
    
    coord_x = r.randrange(-180, 180)
    coord_y = r.randrange(-180, 180)
    hit_x = coord_x
    hit_y = coord_y
    tp_dibuix(coord_x, coord_y - 5)
    
    c.fillcolor("yellow")
    c.begin_fill()
    c.circle(10)
    c.end_fill()

def actualitzar_punts():
    msg.clear()
    msg.write(f"Monedes recolectades: {contador}", align="center", font=("Arial", 18, "bold"))

def game_loop():
    actualitzar_punts()
    if t.distance(hit_x, hit_y) < 20:
        global contador
        t.goto(-150, 0)
        generar_moneda()
        contador += 1
    
    if t.xcor() < -200 or t.xcor() > 200 or t.ycor() < -200 or t.ycor() > 200:
        t.goto(-150, 0)
    
    if contador == 20:
        msg.goto(0, 0)
        msg.write(f"Felicitats, eres ric", align="center", font=("Arial", 30, "bold"))
        msg.goto(0, 250)
        wn.ontimer(msg.clear, 2000)

    wn.update()
    wn.ontimer(game_loop, 20)

wn.listen()
wn.onkeypress(up, "Up")
wn.onkeypress(down, "Down")
wn.onkeypress(left, "Left")
wn.onkeypress(right, "Right")
wn.onkeypress(wn.bye, "Escape")

quadrat()
generar_moneda()

game_loop()
wn.mainloop()
