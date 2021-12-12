# Ejercicio 2
# Escribir una función que reciba un número entero positivo y devuelva su factorial.

def factorial():
    num = int(input("Introduce tu numero entero y positivo: "))
    if num > 0:
        factorial = 1
        for i in range(1, num + 1):
            factorial = factorial * i
        print(factorial)
    else:
        print("Error, numero negativo")

factorial()