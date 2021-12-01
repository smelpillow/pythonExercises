# Solicitar el peso y la estatura para calcular el indice de masa corporal "imc", redondeado a dos decimales

peso = input("¿Cúal es tu peso en kg? ")
estatura = input("¿Cúal es tu estatura en metros? ")
imc = round(float(peso) / float(estatura) ** 2,2)

print("Tu índice de masa corporal es " + str(imc))

# Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <dividendo> entre <divisor> da un 
# cociente <c> y un resto <r> donde <dividendo> y <divisor> son los números introducidos por el usuario, y <c> y <r> son el 
# cociente y el resto de la división entera respectivamente

dividendo = input("Introduce el dividendo (entero): ")
divisor = input("Introduce el divisor (entero): ")
print(dividendo + " entre " + divisor + " da un cociente " + str(int(dividendo) // int(divisor)) + " y un resto " + str(int(dividendo) % int(divisor)))

# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés porcentual anual y el número de años, y 
# muestre por pantalla el capital obtenido en la inversión redondeado con dos decimales

cantidad = float(input("¿Cantidad a invertir? "))
interes = float(input("Interés porcentual anual? "))
años = int(input("¿Años? "))

print("Capital final: " + str(round(cantidad + (interes / 100 + 1) ** años, 2)))