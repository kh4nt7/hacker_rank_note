import turtle as t

wn = t.Screen()
# t.hideturtle()
t.penup()
t.setpos(-50, 50)
t.pendown()
t.colormode(255)
# Draw Yellow Part
t.color(217, 206, 4)
t.begin_fill()
t.forward(200)
t.right(90)
t.forward(40)
t.right(90)
t.forward(200)
t.end_fill()
t.color(46, 212, 0)


# Green Part
t.begin_fill()
t.left(90)
t.forward(40)
t.left(90)
t.forward(200)
t.left(90)
t.forward(40)
t.end_fill()

# Red Part
t.right(180)
t.forward(40)

t.begin_fill()
t.color(255, 41, 73)
t.forward(40)
t.right(90)
t.forward(200)
t.right(90)
t.forward(40)
t.end_fill()

t.penup()
t.color("white")
t.right(90)
# to start draw star
t.setpos(10,1)
t.pendown()
t.begin_fill()
size = 78
for i in range(5):
	t.forward(size)
	t.left(-144)
t.end_fill()
t.penup()
t.goto(55,65)
t.color("black")
t.write("Flag of Myanmar",align="center", font=("Arial", 15, "normal"))
t.hideturtle()
