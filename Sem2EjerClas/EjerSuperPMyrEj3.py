import os
"""
3. Un supermercado ha puesto en oferta la venta al por mayor de cierto producto, ofreciendo un descuento del 15% por la compra de más de 3 docenas y 10% en caso contrario. Además, por la compra de más de 3 docenas se obsequia una unidad del producto por cada docena en exceso sobre 3. Diseñe un programa que determine el monto de la compra, el monto del descuento, el monto a pagar y el número de unidades de obsequio por la compra de cierta cantidad de docenas del producto.
"""
respuesta = 0

def menu_docena_manzanas():
    os.system("cls||clear")
    print("Ingrese la cantidad de docenas de manzanas (c$3500 por docena): ")
    return int(input("Respuesta: "))

def pregunta_seguir():
    os.system("cls||clear")
    print("Desea continuar?")
    print("1. Si")
    print("2. No")
    return int(input("Respuesta: "))

while respuesta != 2:
    docenas = menu_docena_manzanas()
    if docenas > 3:
        descuento = 0.15
        obsequio = docenas - 3
    else:
        descuento = 0.10
        obsequio = 0
    precio = 3500
    subtotal = precio * docenas
    descuento_total = subtotal * descuento
    total = subtotal - descuento_total
    print("-*"*20)
    print("FACTURA")
    print(f"Docenas:\t\t{docenas}")
    print(f"Tipo de descuento:\t{descuento*100:.0f}%")
    print(f"Descuento:\t\tc${descuento_total:,.2f}")
    print(f"Subtotal:\t\tc${subtotal:,.2f}")
    print(f"Total:\t\t\tc${total:,.2f}")
    print(f"Obsequio:\t\t{obsequio} manzanas")
    print("-*"*20)
    input("Presione tecla Enter para continuar...")
    respuesta = pregunta_seguir()
else:
    print("Gracias por usar el sistema")