def sumar(a, b):
    return a + b
def restar(a, b):
    return a - b
def dividir(a, b):
    if b == 0:
        return "Error: División por cero no permitida."
    else:
        return a / b
def multiplicar(a, b):
    return a * b

def saludito():
    nombre = input("Ingrese su nombre: ")
    print(f"Hola {nombre}, bienvenido a la programación en Python.")

def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(0, 13):
        print(f"{numero} x {i} = {numero * i}")
        i+= 1

texto = "Hola mundo"