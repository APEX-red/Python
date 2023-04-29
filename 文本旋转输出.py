import turtle as t
t.color('red')
t.pensize(10)
text='论其可行性'
t.penup()
x=len(text)
for i in text:
    t.write(i,font='consolas')
    t.right(360/x)
    t.penup()
    t.forward(50)
t.hideturtle()
t.done()