import turtle as t
x=-200
y=200
t.speed(999)
t.pensize(5)
t.screensize(500,500)
t.bgcolor('light green')
t.penup()
t.goto(x,y)
for i in range(3):
    t.fillcolor('white')
    for j in range(3):
        t.penup()
        t.goto(x,y)
        t.pendown()
        t.fillcolor('white')
        t.begin_fill()
        for k in range(4):
            t.forward(100)
            t.right(90)
        t.end_fill()
        x=x+140
    y=y-120
    x=-200
t.done()