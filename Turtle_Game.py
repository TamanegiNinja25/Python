import turtle
import random
screen = turtle.Screen()
screen.title("Game Testing Version 1.0")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

p = turtle.Turtle()
p.shape("turtle")
p.color("yellow")
p.penup()
p.speed(4)

t = turtle.Turtle()
t.shape("square")
t.color("red")
t.penup()
t.speed(4)

sw = turtle.Turtle()
sw.hideturtle()
sw.color("white")
sw.penup()
sw.goto(0,260)

score = 0
STEP = 20

def update_score():
    sw.clear()
    sw.write(f"Score: {score}", align="center", font=("Arial", 16, "normal"))

    
def place_target():
    x = random.randint(-260, 260)
    y = random.randint(-260, 260)
    t.goto(x, y)

    
def move_up():
    p.setheading(90)
    p.forward(STEP)

    
def move_down():
    p.setheading(270)
    p.forward(STEP)

    
def move_left():
    p.setheading(180)
    p.forward(STEP)

    
def move_right():
    p.setheading(0)
    p.forward(STEP)

    
def try_catch():
    global score
    if p.distance(t) < 20:
        score += 1
        update_score()
        place_target()

        
def quit_game():
    screen.bye()

    
screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey(try_catch, "space")
screen.onkey(quit_game, "q")

place_target()
update_score()
while True:
    screen.update()

