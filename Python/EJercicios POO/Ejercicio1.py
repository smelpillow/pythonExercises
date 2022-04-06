# Realizar un programa que conste de una clase llamada Estudiante, que tenga como atributos el nombre y la nota del alumno. 
# Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

class Estudiante():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    
    def imprimir(self):
        print("Nombre: {} \nNota: {}".format(self.nombre, self.nota))

    def resultado(self):
        if self.nota < 7:
            print("Has suspendido")
        else:
            print("Has aprovado")
    
estudiante1 = Estudiante("Manel Artero", 10)
estudiante1.imprimir()
estudiante1.resultado()

estudiante2 = Estudiante("Lo Man", 6)
estudiante2.imprimir()
estudiante2.resultado()