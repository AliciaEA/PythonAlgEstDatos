respuesta = 0
def menu():
    print("Menu")
    print("1.Calcular la serie numerica 1+3+5+...+n")
    print("2. Calcular 1*3*5*...*n")
    print("3. Salir")
    opcion = int(input("Ingrese una opcion: ")) 
    return opcion
    
def ingresar_numero():
    n = int(input("Ingrese un numero: "))
    return n

while(respuesta != 3):
    opcion = menu()
    match opcion:
        case 1:
            n = ingresar_numero()
            if n%2 != 0:
                continue
            suma = 0
            for i in range(1, n+1, 2):
                suma += i
            print(f"La suma de la serie numerica es: {suma}")
        case 2:
            n = ingresar_numero()
            if n%2 != 0:
                continue
            producto = 1
            for i in range(1, n+1, 2):
                producto *= i
            print(f"El producto de la serie numerica es: {producto}")
        case 3:
            print("Saliendo...")
        case _:
            print("Opcion no valida.")


