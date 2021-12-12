# En la siguiente lista, debes hacer un programa que muestre los valores al usuario, a su vez, debe pedir dos datos y esos que sean ingresados deben ser sustituidos en el primer y segundo lugar:
# [20, 50, "Curso", 'Python', 3.14]

# Mostrar valores, ingresar datos en primer segundo espacio

lista = [20, 50, "Curso", 'Python', 3.14]

print("Esta es la lista actual --> ", lista)

datos = input("Primer dato: ")
datos2 = input("Segundo dato: ")

''' lista.insert(2, datos)
lista.insert(3, datos2)

print("Asi queda la lista ahora --> ",lista)  '''

lista[0] = datos
lista[1] = datos2

print("Asi queda la lista ahora --> ",lista)