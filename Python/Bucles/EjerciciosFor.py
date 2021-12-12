# Ejercicio 1
# Imprimir por pantalla los numeros del 1 al 10, luego, pedir al usuario dos numeros y mostrar el rango de numeros entre ambas cifras

for i in range(1,11):
    print(i)

cifra1 = int(input("Introduce la primera cifra: "))
cifra2 = int(input("Introduce la segunda cifra: "))

for i in range(cifra1,cifra2+1):
    print(i)

# Ejercicio 2
# Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.