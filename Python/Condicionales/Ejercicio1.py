# Crear un programa que pida al usuario una letra, y si es vocal, muestre el mensaje "Es vocal". Sino, decirle al usuario que no es vocal

letra = input("Introduce una vocal: ")

if letra.lower() == "a":
    print ("Has escrito una VOCAL")
elif letra.lower() == "e":
    print ("Has escrito una VOCAL")
elif letra.lower() == "i":
    print ("Has escrito una VOCAL")
elif letra.lower() == "o":
    print ("Has escrito una VOCAL")
elif letra.lower() == "u":
    print ("Has escrito una VOCAL")
else:
    print ("Eres un GENTUZO y no conoces las vocales")

if letra.lower() == "a":
    print ("Has escrito una VOCAL")
else:
    if letra.lower() == "e":
        print ("Has escrito una VOCAL")
    else:
        if letra.lower() == "i":
            print ("Has escrito una VOCAL")
        else:
            if letra.lower() == "o":
                print ("Has escrito una VOCAL")
            else:
                if letra.lower() == "u":
                    print ("Has escrito una VOCAL")
                else:
                    print ("Eres un GENTUZO y no conoces las vocales")

if letra.lower() in "aeiou":
    print ("Has escrito una Vocal")
else:
    print ("No has escrito una vocal")