Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> ts = turtle.getscreen()
>>> t = turtle.Turtle()
>>> t.color("blue")
>>> t.begin_fill()
>>> t.circle(50)
t.e
>>> t.end_fill()
>>> t.penup()
>>> t.pendown()
>>> t.forward(60)
>>> t.forward(100)
>>> t.color("red")
>>> t.begin_fill()
>>> t.circle(50)
>>> t.end_fill()
>>> t.right()
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    t.right()
TypeError: TNavigator.right() missing 1 required positional argument: 'angle'
>>> t.right(90)
>>> t.forward(100)
>>> t.color("green")
>>> t.begin_fill()
>>> t.circle(50)
t.en
>>> t.end_fill()
>>> t.left(90)
>>> t.right(180)
>>> t.forward(100)
>>> t.forward(60)
>>> t.color("yellow")
>>> t.begin_fill()
>>> t.circle(50)
>>> t.end_fill()
>>> t.right(90)
>>> t.forward(100)
