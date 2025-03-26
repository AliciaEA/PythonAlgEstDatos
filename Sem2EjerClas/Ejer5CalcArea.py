import os
import math

"""
. Se desea escribir un programa para el cálculo del área de diversas superficies: cuadrado, rectángulo, círculo, triángulo y trapecio. El programa mostrará al inicio el siguiente menú:

****

Seguidamente leerá de la entrada estándar un valor que estará comprendido entre 1 y 5, indicando el tipo de superficie cuya área se desea calcular.  El programa leerá entonces los datos que necesite para calcular el área en cuestión.  El resultado se mostrará en la salida estándar, tras lo cual el programa terminará.

-	Implementa estructuras repetitivas de tal forma que los programas se ejecuten mientras el usuario lo desea.

"""

respuesta = 0

#MENU DE AREAS
def menu_area():
    os.system("cls||clear")
    print("="*40)
    print("CALCULO DE SUPERFICIES (version 1.0)")
    print("="*40)
    print("1. Cuadrado")
    print("2. Círculo")
    print("3. Rectángulo")
    print("4. Trapecio")
    print("5. Triángulo")
    print("="*40)
    return int(input("Respuesta: "))

#Preguntar si continuar en el programa o salir
def pregunta_seguir():
    os.system("cls||clear")
    print("Desea continuar?")
    print("1. Si")
    print("2. No")
    return int(input("Respuesta: "))

def calc_area_cuadrado():
    lado = float(input("Ingrese el lado del cuadrado (cm): "))
    return lado**2
def calc_area_circulo():
    radio = float(input("Ingrese el radio del círculo (cm): "))
    return math.pi * radio**2
def calc_area_rectangulo():
    base = float(input("Ingrese la base del rectángulo (cm): "))
    altura = float(input("Ingrese la altura del rectángulo (cm): "))
    return base * altura
def calc_area_trapecio():
    base_mayor = float(input("Ingrese la base mayor del trapecio (cm): "))
    base_menor = float(input("Ingrese la base menor del trapecio (cm): "))
    altura = float(input("Ingrese la altura del trapecio (cm): "))
    return (base_mayor + base_menor) * altura / 2
def calc_area_triangulo():
    base = float(input("Ingrese la base del triángulo (cm): "))
    altura = float(input("Ingrese la altura del triángulo (cm): "))
    return base * altura / 2
    

while respuesta != 2:
    respuesta = menu_area()

    match respuesta:
        case 1:
            print(f"El área del cuadrado es: {calc_area_cuadrado():.2f}cm²")
        case 2:
            print(f"El área del círculo es: {calc_area_circulo():.2f}cm²")
        case 3:
            print(f"El área del rectángulo es: {calc_area_rectangulo():.2f}cm²")
        case 4:
            print(f"El área del trapecio es: {calc_area_trapecio():.2f}cm²")
        case 5:
            print(f"El área del triángulo es: {calc_area_triangulo():.2f}cm²")
        case _:
            print("Sorry no es valido chikitin")
    input("Presione tecla Enter para continuar...")
    respuesta = pregunta_seguir()
else:
    print("Gracias por usar el sistema")

