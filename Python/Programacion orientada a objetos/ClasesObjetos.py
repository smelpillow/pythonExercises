from re import T


class FabricaTelefonos():
    pass

print(type(FabricaTelefonos))

celular = FabricaTelefonos()
celular2 = FabricaTelefonos()

print(type(celular))
print(type(celular2))

def FabricaTelefonos(): # Atencion... no definir el mismo nombre por mucho que sean dos objetos diferentes
    pass

print(type(FabricaTelefonos()))