# Ejercicio 1 del Sistematico de Python 09/04/2025

# Alicia Massiel Estrada Acevedo - Version 1.0

import os
import modulo1 as mod1 #importando modulo
import clase as estud

lista_estudiantes = []
respuesta = 0

while respuesta != 5:  # Bucle para validar si la opción es válida
    try:
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar la consola
        opcion = mod1.menu_opciones() #llamando a la funcion menu_opciones del modulo1
    except ValueError:
        
        print("Error: Debe ingresar un número entero. Intente nuevamente.") #Imprimiria que dio error
        input()
        continue
    
    match opcion:
        case 1:
            #Pedimos el nombre del estudiante
            nombre = input("Ingrese el nombre del estudiante: ")
           
            try: #Verificamos que la edad sea int
                edad = int(input("Ingrese la edad del estudiante: "))
            except ValueError:
                print("Error: Debe ingresar un número entero. Intente nuevamente.") #Imprimiria que dio error
                continue
            
            if edad <= 0:  # Verificar que la edad sea positiva
                print("Error: La edad debe ser un número positivo. Intente nuevamente.")
                continue
            carrera = input("Ingrese la carrera dle estudiante: ")
            
            estudiante = estud.Estudiante(nombre.upper(), edad, carrera)
            lista_estudiantes.append(estudiante)
            
            print("estudiante agregado correctamente")
            input()
            continue
        case 2:
            nombre_buscar= input("Ingrese el nombre a buscar: ").upper()
            estudiante = mod1.buscar_estudiante(nombre_buscar, lista_estudiantes)
            if estudiante:
                print("Estudiante encontrado:")
                try: #Verificamos que la edad sea int
                    calificacion = float(input(f"Agregue la calificacion al estudiante {estudiante.nombre}: "))
                    estudiante.agregar_calificacion(calificacion)
                    print("Calificacion agregada correctamente")
                except ValueError:
                    print("Error: Debe ingresar un número entero. Intente nuevamente.") #Imprimiria que dio error
                    continue
                
            else:
                print("Estudiante no encontrado.")
                input()
                continue
                
                input()
            
            
            input()   
            
        case 3:
            nombre_buscar = input("Ingrese el nombre del estudiante a buscar: ").upper()
            
            estudiante = mod1.buscar_estudiante(nombre_buscar, lista_estudiantes)
            if estudiante:
                print("Estudiante encontrado:")
                estudiante.mostrar_info()  # Llamar al método mostrar_info de la clase Estudiante
                input()
            else:
                print("Estudiante no encontrado.")
                input()
                continue
               

        case 4:
            if len(lista_estudiantes) == 0:  # Verificar si la lista está vacía
                print("No hay estudiantes registrados.")
            else:
                print("Lista de estudiantes registrados:")
                for estudiante in lista_estudiantes:
                    estudiante.mostrar_info()  # Llamar al método mostrar_info de cada estudiante
                    print("-" * 20)  # Separador entre estudiantes
            
            input("Presione Enter para continuar...")
        case _:
            print("Uy esa no es una opcion")
    respuesta = 1
            
            
            
