import turtle
colors=["green","white","orange"]
t=turtle.Pen()
turtle.bgcolor("black")
for i in range(200):
    t.pencolor(colors[i%3])
    t.width(i/100+1)
    t.forward(i)
    t.left(i)