# Escribir una tupla con los meses del año, luego, pide al usuario un numero, el que haya ingresado, es el mes que debe mostrar en la tupla

meses = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')

dato = int(input("Introduce el numero de mes: "))

print (meses[dato - 1])

# Escribir una tupla que tenga las letras del alfabeto. Luego, debes pedir al usuario un número, el que haya ingresado, es la letra que debe imprimir el programa

letras = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')

opcionLetra = int(input("Introduce un num de letra hasta el 8: "))
print (letras[opcionLetra - 1])