try:
    Num=float(input("Ingresa un numero: "))
    print('Tu numero es: ',Num)
except:
    print("No has ingresado un numero")

while(True):
    try:
        Num=float(input("Ingresa un numero: "))
        print('Tu numero es: ',Num)
        break
    except:
        print("No has ingresado un numero")