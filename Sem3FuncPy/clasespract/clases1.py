#ejemplificando clases en python
import modulo as mod #importando modulo

        
alumno = mod.Alumno(input("Ingresua tu nombre: "), int(input("Tu edad: "))) #instancia de la clase Alumno
alumno.saludar()

mod.Alumno.saludar(alumno) # forma alternativa de llamar al metodo


nombre = input("Ingrese el nombre del perro: ")
raza = input("Ingrese la raza del perro: ")
altura = float(input("Ingrese la altura del perro: "))
perro = mod.Perro(nombre, raza, altura) #instancia de la clase Perro
perro.comer()
perro.ladrar()
perro.dormir()

