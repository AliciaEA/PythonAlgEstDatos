import modulo as mod #importando modulo

nombre = input("Ingrese el nombre del estudiante: ")
nota = float(input("Ingrese la nota del estudiante: "))

estudiante = mod.Estudiante(nombre, nota) #instancia de la clase Estudiante
estudiante.mostrarNota()
        
        