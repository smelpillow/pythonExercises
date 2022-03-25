from ast import AsyncFunctionDef


while True:
    try:
        edad = int(input("Ingrese tu edad: "))
        print("Tu edad es: ", edad)
        break
    except:
        print("Has puesto un valor erroneo")
    finally:
        print("El programa se ha ejecutado correctamente")