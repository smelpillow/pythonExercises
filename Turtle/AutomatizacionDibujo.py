import turtle
from unittest import result

s = turtle.Screen()
t = turtle.Turtle()

for i in range(4):
    t.forward(100)
    t.right(90)

t.clear()

resultado = input("Quieres imprimir una figura?")
if resultado == "si":
    while i <= 100:
        t.speed(10)
        t.circle(i)
        i += 10
else:
    print("Ok")

turtle.done()