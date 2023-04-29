import turtle as t
t.screensize(500,500)
t.penup()
t.pensize(5)
t.pendown()
for j in range (6):
    t.right(60)
    for i in range (2):
        t.forward(100)
        t.right(60)
        t.forward(100)
        t.right(120)
t.done()