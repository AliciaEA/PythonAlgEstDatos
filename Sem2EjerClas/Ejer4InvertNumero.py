import os
"""
4. Diseñe un programa que lea un número de tres cifras y determine si es igual al revés del número. Ejemplo: 121 es igual a 121, 123 no es igual a 321.
"""
respuesta = 0

def invertir_numero(numero):
    # Convertir el número a cadena e invertirlo
    numero_invertido = int(str(numero)[::-1]) # [::-1] invierte la cadena (Manipulacion de Strings)
    # Comparar el número original con el invertido
    print(f"El número original es:\t{numero}")
    print(f"El número invertido es:\t{numero_invertido}")
    return numero == numero_invertido

def es_numero_tres_cifras(numero):
    #abs() retorna el valor absoluto de un número
    return 100 <= abs(numero) <= 999 #Comparac. encadenada(valor1 <= valor2 and valor2 <= valor3)

def pregunta_seguir():
    os.system("cls||clear")
    print("Desea continuar?")
    print("1. Si")
    print("2. No")
    return int(input("Respuesta: "))

while respuesta != 2:
    os.system("cls||clear")
    # Leer un número de tres cifras
    numero = int(input("Ingrese un número de tres cifras: "))
    if not es_numero_tres_cifras(numero):
        print("\nEl número ingresado no es de tres cifras.")
        input("\n\nPresione tecla Enter para continuar...")
        continue
    # Verificar si es igual al revés
    if invertir_numero(numero):
        print(f"\nEl número {numero} es igual al revés.")
    else:
        print(f"\nEl número {numero} no es igual al revés")

    input("\nPresione tecla Enter para continuar...")
    respuesta = pregunta_seguir()
else:
    print("Gracias por usar el sistema")
