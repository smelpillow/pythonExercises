class FabricaTelefonos():
    def __init__(self, marca, *colores, **modelos):
        self.marca = marca
        self.colores = colores
        self.modelos = modelos

telefono = FabricaTelefonos("Nokia", "Rojo", "Verde", v1 = 500, v2 = 600)
print(telefono.marca)
print(telefono.colores)
print(telefono.modelos)
# Crear un atributo temporal
telefono.memoria = 512
print(telefono.memoria)