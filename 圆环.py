import turtle as t
i=2
r=50
t.color('blue')
for i in range(i):
    t.fillcolor('black')
    t.begin_fill()
    t.circle(r)
    t.penup()
    t.sety(-r)
    t.pendown()
    r=r+50
    t.end_fill()
t.done()