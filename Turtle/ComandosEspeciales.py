import turtle

s = turtle.Screen()
t = turtle.Turtle()

t.speed(10)
t.circle(10)
t.speed(10)
t.circle(50)
t.dot(30)

t.hideturtle()
t.circle(90)

t.showturtle()
t.backward(200)

t.setx(100)
t.sety(-300)

turtle.done()