import random

name = input("Cual es tu nombre? ")
question = input("Cual es la pregunta? ")
randomNumber = random.randint(1, 10)
answer = ""

if randomNumber == 1:
 answer = "Sí, definitivamente!"
elif randomNumber == 2:
 answer = "Por supuesto que sí"
elif randomNumber == 3:
 answer = "Sin lugar a dudas"
elif randomNumber == 4:
 answer = "No se yo, vuelve a probar"
elif randomNumber == 5:
 answer = "Preguntame mas tarde"
elif randomNumber == 6:
 answer = "Mejor no responderte"
elif randomNumber == 7:
 answer = "Me dice por ahí que no"
elif randomNumber == 8:
 answer = "Muy dudoso"
elif randomNumber == 9:
 answer = "Seguro que no"
elif randomNumber == 10:
 answer = "Tu sabes contar? Pues no cuentes con ello"
else:
 answer = "Error"

print(name + " pregunta: " + question)
print("La bola mágica del 8 dice: " + answer + " El numero era --> " + str(randomNumber))