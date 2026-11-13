Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import turtle
ts = turtle.getscreen()
t = turtle.Turtle()
t.speed(5)
t.pensize(3)

def move_east():
    t.penup()
    t.setheading(0)
    t.fd(100)

    
def move_north():
    t.penup()
    t.setheading(90)
    t.fd(100)

    
def move_left():
    t.penup()
    t.setheading(180)
    t.fd(100)

    
def move_south():
    t.penup
    t.setheading(270)
    t.fd(100)
... 
...     
>>> def draw_square():
...     t.pendown()
...     for i in range(4):
...         t.fd(50)
...         t.rt(90)
...     t.penup()
... 
...     
>>> def draw_circle():
...     t.pendown()
...     t.circle(50)
...     t.penup()
... 
...     
>>> def draw_hexagon():
...     t.pendown()
...     for i in range(6):
...         t.fd(40)
...         t.rt(60)
...     t.penup()
... 
...     
>>> def draw_house():
...     t.pendown()
...     for i in range(4):
...         t.fd(60)
...         t.rt(90)
...     t.penup()
...     t.setheading(90)
...     t.fd(60)
...     t.pendown()
...     t.setheading(0)
...     for i in range(3):
...         t.fd(60)
...         t.lt(120)
...     t.penup()
... 
...     
>>> def reset_screen():
...     t.penup()
...     t.clear()
...     t.home()
... 
...     
>>> screen = turtle.Screen()
>>> screen.listen()
>>> screen.onkey(move_north, "Up")
>>> screen.onkey(move_south, "Down")
>>> screen.onkey(move_left, "Left")
>>> screen.onkey(move_east, "Right")
>>> screen.onkey(draw_square, "S")
>>> screen.onkey(draw_circle, "c")
>>> screen.onkey(draw_hexagon, "h")
>>> screen.onkey(draw_house, "i")
>>> screen.onkey(reset_screen, "r")
>>> 
>>> screen.mainloop()
