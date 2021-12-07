# Se desea tener un algoritmo que permita determinar y mostrar el promedio que ha obtenido un alumno en un determinado curso, conociendo las notas de: tres prácticas, el examen parcial y el examen final.
# Considere:
# PP = ( P1 + P2 +P3 ) / 3 PROM = ( PP + 2*EP + 3*EF ) / 6
# Donde: P1, P2, P3 : Practicas
# PP: promedio de práctica
# PROM: promedio
# EP: examen parcial
# EF: examen final

Practica1 = float(input("Introduce la nota de Practica 1: "))
Practica2 = float(input("Introduce la nota de Practica 2: "))
Practica3 = float(input("Introduce la nota de Practica 3: "))
ExamenParcial = float(input("Introduce la nota del Examen Parcial: "))
ExamenFinal = float(input("Introduce la nota del Examen Final: "))

PromedioPractica = (Practica1 + Practica2 + Practica3) / 3
Promedio = (PromedioPractica + 2*ExamenParcial + 3*ExamenFinal) / 6

print ("El alumno ha conseguido un Promedio de Practica de: ", PromedioPractica)
print ("El alumno ha conseguido un Promedio Final de :", Promedio)