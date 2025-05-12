from Cola import Cola
from colorama import Fore, Style

cola = Cola()
respuesta = 0

def pausa():
    input(Fore.YELLOW + "Presione Enter para continuar..." + Style.RESET_ALL)
def limpiar_pantalla():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

while respuesta != 4:
    limpiar_pantalla()
    print(Fore.MAGENTA + "\nMenú de opciones:" + Style.RESET_ALL)
    print(Fore.YELLOW + "======================" + Style.RESET_ALL)
    print(Fore.YELLOW + "1. Insertar dato" + Style.RESET_ALL)
    print(Fore.YELLOW + "2. Eliminar dato" + Style.RESET_ALL)
    print(Fore.YELLOW + "3. Imprimir" + Style.RESET_ALL)
    print(Fore.YELLOW + "4. Salir" + Style.RESET_ALL)
    
    try:
        respuesta = int(input("Seleccione una opción: "))
        
    except ValueError:
        print("Error: Debe ingresar un número entero.")
        pausa()
        continue
        
    match respuesta:
        case 1:
            try:
                dato = int(input("Ingrese un dato: "))
            except ValueError:
                print(Fore.RED + "Error: Debe ingresar un número entero." + Style.RESET_ALL)
                pausa()
                continue
            cola.Insetar(dato)
            print(Fore.GREEN + "\nDato insertado correctamente." + Style.RESET_ALL)
            pausa()
            
        case 2:
            dato_eliminado = cola.Eliminar()
            if dato_eliminado is not None:
                print(Fore.RED + f"\nDato eliminado: {dato_eliminado}" + Style.RESET_ALL)
            else:
                print(Fore.RED + "Cola vacía, no se puede eliminar." + Style.RESET_ALL)
            pausa()
        case 3:
            print(Fore.CYAN + "\nContenido de la cola:" + Style.RESET_ALL)
            cola.Imprimir()
            pausa()
                
        case 4:
            print(Fore.BLUE + "Saliendo del programa..." + Style.RESET_ALL)
            pausa()
            break
            
        case _:
            print(Fore.RED + "Opción no válida, intente nuevamente." + Style.RESET_ALL)
            pausa()
            continue
            
    

