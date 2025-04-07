# Ejemplificando funciones python
import modulos as mod
from modulos import multiplicar, sumar, restar, dividir


mod.saludito()
print("Ejemplificando funciones python")
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
resultado = sumar(num1, num2)
print(f"La suma de {num1} y {num2} es: {resultado}")
print("*"*30)
print(f"El resultado de la resta es: {restar(num1, num2)}")
print(f"El resultado de la multiplicación es: {multiplicar(num1, num2)}")
print(f"El resultado de la división es: {dividir(num1, num2)}")

print("crazy")
print(mod.texto)