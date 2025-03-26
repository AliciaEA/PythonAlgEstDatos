import os

"""
1.Desarrolla un programa que calcule el importe a pagar por un vehículo al circular por una autopista. El vehículo puede ser una bicicleta, una moto, un carro o un camión. Para definir el conjunto de vehículos deben utilizar una estructura adecuada. El importe se calculará según los siguientes datos:

a) Un importe fijo de 100 córdobas para la bicicleta.
b) Las motos y los carros pagarán 30 córdobas por Km.
c) Los camiones pagarán 30 córdobas por Km. más 25 córdobas por toneladas.
"""

respuesta = 0

def obtener_respuesta_vehiculo():
    os.system("cls||clear")
    print("Ingrese el tipo de vehiculo")
    print("1. Bicicleta")
    print("2. Moto o Carro")
    print("3. Camiones")
    return int(input("Respuesta: "))

def pregunta_seguir():
    os.system("cls||clear")
    print("Desea continuar?")
    print("1. Si")
    print("2. No")
    return int(input("Respuesta: "))

while respuesta != 2: 
    vehiculo = obtener_respuesta_vehiculo()

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

    input("Presione tecla Enter para continuar...")
    respuesta = pregunta_seguir()
else:
    print("Gracias por usar el sistema")

