import os

"""
2. Escribir un programa que permita emitir la FACTURA correspondiente, a una compra de un artículo determinado, del que se adquieren una o varias unidades. El IVA a aplicar es de 15% y si el Sub Total (precio de venta por cantidad), es mayor de 1000, se aplicará un descuento del 12%.
"""
respuesta = 0

def obtener_respuesta_articulo():
    os.system("cls||clear")
    print("Ingrese el tipo de articulo")
    print("1. Pequeño Peluche de Osito\t\tc$350")
    print("2. Mediano Peluche de Ballena\t\tc$560")
    print("3. Grande Peluche de Perro\t\tc$800")
    return int(input("Respuesta: "))

def obtener_total(precio):
    cantidad = int(input("Ingrese la cantidad de articulos: "))
    subtotal = cantidad * precio
    iva = subtotal * 0.15
    total = subtotal + iva
    if subtotal > 1000:
        descuento = total * 0.12
        total = total - descuento
    else:
        descuento = 0
    print("-*"*20)
    print("FACTURA")
    print(f"Descuento:\t\tc${descuento:.2f}")
    print(f"Subtotal:\t\tc${subtotal:.2f}")
    print(f"IVA:\t\t\tc${iva:.2f}")
    print(f"Total:\t\t\tc${total:.2f}")
    print("-*"*20)

def pregunta_seguir():
    os.system("cls||clear")
    print("Desea continuar?")
    print("1. Si")
    print("2. No")
    return int(input("Respuesta: "))

while respuesta != 2:
    articulo = obtener_respuesta_articulo()
    match articulo:
        case 1:
            precio = 350
            obtener_total(precio)
           
        case 2:
            precio = 560
            obtener_total(precio)
        case 3:
            precio = 800
            obtener_total(precio)
        case _:
            print("Sorry no es valido chikitin")

    input("Presione tecla Enter para continuar...")
    respuesta = pregunta_seguir()
else:
    print("Gracias por usar el sistema")
