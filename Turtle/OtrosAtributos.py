import turtle

s = turtle.Screen()
t = turtle.Turtle()

'''t.begin_fill()
t.circle(100)
t.end_fill()

t.begin_fill()
t.color("White", "White")
t.circle(50)
t.end_fill()'''

t.shape("turtle")

t.penup()
t.forward(100)
t.pendown()
t.right(90)
t.forward(100)
t.penup()
t.backward(100)
t.pendown()
t.left(90)
t.forward(100)

t.undo()
t.clear()
t.reset()

t.forward(100)
t.stamp()
t.forward(100)

turtle.done()