"""
MATCH CASE
Ejercicio: Cálculo de tarifas de envío
El usuario elige el tipo de paquete y la distancia a enviar. El programa calcula el importe a pagar según estas tarifas:

Carta o Documento → ₡5 por km

Pequeño Paquete (menos de 5kg) → ₡10 por km

Paquete Grande (más de 5kg) → ₡15 por km + ₡5 extra por kg adicional
"""

def ingresoDistancia():
    return float(input("Ingrese la distancia a enviar(km): "))

def ingresoPeso():
    return float(input("Ingrese el peso del paquete(kg): "))
print("-*"*25)


print("-*"*25)

print("Escoge el paquete que deseas adquirir")
print("1. Carta o Documento → ₡5 por km")
print("2. Pequeño Paquete (menos de 5kg o 5kg) → ₡10 por km")
print("3. Paquete Grande (más de 5kg) → ₡15 por km + ₡5 extra por kg adicional")

tipoPaquete = int(input(": "))

match tipoPaquete:
    case 1: 
        distancia = ingresoDistancia()
        costo = distancia * 5
        print(f"El costo de envío es de c${costo}")
    case 2:
        distancia = ingresoDistancia()
        peso = ingresoPeso()
        if peso <=5:
            costo = distancia * 10
            print(f"El costo de envío es de c${costo}")
        else:
            print("El paquete es muy pesado")
    case 3:
        distancia = ingresoDistancia()
        peso = ingresoPeso()
        if peso >= 5:
            costo = distancia * 15 + (peso - 5) * 5
            print(f"El costo de envío es de c${costo}")
        else:
            print("El paquete es muy liviano")
    case _:
        print("Opción no válida")
        


