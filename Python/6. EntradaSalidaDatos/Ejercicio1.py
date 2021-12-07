# Realizar un programa que haga el proceso de formula general para la resolución de ecuaciones, sabiendo que la formula general es la que está en la imagen, el usuario debe ingresar los valores de “a”, “b” y “c”, y el programa debe hacer el proceso para que al final muestre el mensaje: “La solución es: <solucion>”
from math import sqrt # Función de raiz cuadrada
datoa = int(input('Introduce el valor \"A\": '))
datob = int(input('Introduce el valor \"B\": '))
datoc = int(input('Introduce el valor \"C\": '))
x1 = 0
x2 = 0
if ((datob**2)-(4*datoa*datoc)) < 0 :
    print ("No se puede realizar porque no se puede sacar raiz a un numero negativo")
else:
    x1 = (-datob + sqrt((datob**2)-(4*datoa*datoc)))/(2*datoa)
    x2 = (-datob - sqrt((datob**2)-(4*datoa*datoc)))/(2*datoa)
    print ("La solucion es: \nx1=",x1, "\nx2=",x2)