import os
import modulos as mod
#Ejemplificando funciones parametizadas

#Funcion que permita obtener el producto de 2 #


print("*"*30)
os.system("cls||clear")
print("Ejemplificando funciones parametizadas")
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
resultado = mod.multiplicar(num1, num2)
print(f"El producto de {num1} y {num2} es: {resultado}")
print("*"*30)
#Obtener la tabla de multiplicar de un numero



print("*"*30)
print("Ejemplificando funciones parametizadas")
num = int(input("Ingrese un número para obtener su tabla de multiplicar: "))
mod.tabla_multiplicar(num)
print("*"*30)