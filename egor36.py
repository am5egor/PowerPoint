from turtle import *

def move(x,y):
    Dobbi.penup()
    Dobbi.goto(x,y)
    Dobbi.pendown()

def move_left():
    Dobbi.goto(Dobbi.xcor()-5, Dobbi.ycor())

def move_right():
    Dobbi.goto(Dobbi.xcor()+5, Dobbi.ycor())

def move_up():
    Dobbi.goto(Dobbi.xcor(), Dobbi.ycor()+5)

def move_down():
    Dobbi.goto(Dobbi.xcor(), Dobbi.ycor()-5)

def p_col1():
    Dobbi.color('yellow')

def p_col2():
    Dobbi.color('green')

def p_col3():
    Dobbi.color('blue')

def p_col4():
    Dobbi.color('red')

def p_col5():
    Dobbi.color('pink')

def p_col6():
    Dobbi.color('purple')

def p_col7():
    Dobbi.color('skyblue')

def p_col8():
    Dobbi.color('brown')

def p_col9():
    Dobbi.color('orange')

def p_col0():
    Dobbi.color('black')

def s_col1():
    scr.bgcolor('yellow')

def s_col2():
    scr.bgcolor('green')

def s_col3():
    scr.bgcolor('blue')

def s_col4():
    scr.bgcolor('red')

def s_col5():
    scr.bgcolor('pink')

def s_col6():
    scr.bgcolor('purple')

def s_col7():
    scr.bgcolor('skyblue')

def s_col8():
    scr.bgcolor('brown')

def s_col9():
    scr.bgcolor('orange')

def s_col0():
    scr.bgcolor('black')



Dobbi = Turtle()

Dobbi.shape('circle')
Dobbi.pensize(2)

scr = Dobbi.getscreen()
scr.listen()

scr.onscreenclick(move)
scr.onkey(move_left, 'Left')
scr.onkey(move_right, 'Right')
scr.onkey(move_up, 'Up')
scr.onkey(move_down, 'Down')

choise = 'pen'

if choise == 'pen':
    scr.onkey(p_col1, '1')
    scr.onkey(p_col2, '2')
    scr.onkey(p_col3, '3')
    scr.onkey(p_col4, '4')
    scr.onkey(p_col5, '5')
    scr.onkey(p_col6, '6')
    scr.onkey(p_col7, '7')
    scr.onkey(p_col8, '8')
    scr.onkey(p_col9, '9')
    scr.onkey(p_col0, '0')
else:
    scr.onkey(s_col1, '1')
    scr.onkey(s_col2, '2')
    scr.onkey(s_col3, '3')
    scr.onkey(s_col4, '4')
    scr.onkey(s_col5, '5')
    scr.onkey(s_col6, '6')
    scr.onkey(s_col7, '7')
    scr.onkey(s_col8, '8')
    scr.onkey(s_col9, '9')
    scr.onkey(s_col0, '0')

exitonclick()