class Animeles():
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def hablar(self):
        print(self.mensaje)

class Perro(Animeles):
    def hablar(self):
        print("Yo hago guau!")

class Pez(Animeles):
    def hablar(self):
        print("Yo no hablo")

perro = Perro("Guau!")
perro.hablar()

animal = Animeles("Miau!")
animal.hablar()

pez = Pez("Glu glu")
pez.hablar()
