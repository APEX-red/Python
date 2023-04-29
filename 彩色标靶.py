import turtle as t
t.setup(600,500,450,50)
t.pensize(5)
t.bgcolor('white')
t.speed('fastest')
colors = ['blue','yellow','red','green','white','black','orange','grey']
for i in range(10,1,-1):
    t.penup()
    t.goto(0,-20 * i)
    t.pendown()
    t.begin_fill()
    t.fillcolor(colors[i % 4])
    t.circle(20*i)
    t.end_fill()
t.hideturtle()
t.done()