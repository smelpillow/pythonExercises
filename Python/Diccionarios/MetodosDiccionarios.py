diccionario = {1 : 2, 2:3,3:4}
diccionario2 = {5:6, 7:8}
print(diccionario)
diccionario.pop(3) # Elimina la key del diccionario
print(diccionario)
print(diccionario.get(2)) # nos devuelve el valor de la clave 2
print(diccionario)
diccionario.setdefault(4, 5) # Añadir clave y valor
print(diccionario)
diccionario.update(diccionario2) # Añade otro diccionario a los datos
print(diccionario)
diccionario.copy() # Añade una copia del diccionario
print(diccionario)
diccionario.clear() # Elimina todos los datos del diccionario
print(diccionario)