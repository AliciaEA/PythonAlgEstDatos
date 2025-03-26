import os

respuesta = 0
while respuesta != 2: 
    os.system("cls||clear")
    print("Bienvenido al sistema de cobro de peaje")
    print("Ingrese el tipo de vehiculo")
    print("1. Bicicleta")
    print("2. Moto o Carro")
    print("3. Camiones")
    vehiculo = int(input("Respuesta: "))

    match vehiculo:
        case 1:
            importe = 100
            print(f" El importe a pagar es: c${importe}")
        case 2:
            distancia = float(input("Ingrese la distancia recorrida(km): "))
            importe = 20*distancia
            print(f"El importe a pagar es de c${importe:.2f}")
        case 3: 
            distancia = float(input("Ingrese la distancia recorrida(km): "))
            peso = float(input("Ingrese el peso del camion por tonelada: "))
            importe = (distancia * 30)+ (peso * 25)
            print(f"El importe a pagar es de c${importe:.2f}")
        case _:
            print("Sorry no")

    input("Presione cualquier tecla para continuar...")
    os.system("cls||clear")
    print("Desea continuar?")
    print("1. Si")
    print("2. No")
    respuesta = int(input("Respuesta: "))
else:
    print("Gracias por usar el sistema")