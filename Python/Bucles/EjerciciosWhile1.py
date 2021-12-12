# Escribir un programa que pida un numero al usuario y muestre las tablas de multiplicar de ese numero

entrada = int(input("Introduce un numero: "))
i = 0
calculo = 0

while i <= 10:
    calculo = entrada * i
    print ("{} x {} = {}".format(entrada, i, calculo))
    i += 1

# Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

edad = int(input("Introduce tu edad: "))
i = 1

while i != edad:
    print ("Has cumplido {} años".format(i))
    i += 1