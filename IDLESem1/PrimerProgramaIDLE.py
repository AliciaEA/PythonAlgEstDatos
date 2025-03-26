#Mi primer programa Python
print("+-"*25)
print("Bienvenido a Python")
print("UAM")
print("+-"*25)

usuario = input("Como quieres que te llame?: ")

numero1 = int(input("Escribe un numero  pa sumarlo: "))
numero2 = int(input("Escribe otro numero  pa sumarlo:"))

print(numero1+numero2)

print("-"*30)

base = int(input("Pon la base de la potencia: "))
potencia = int(input("Ahora el exponente: "))
print(base**potencia)

print("-"*30)

print("Division de preferiblemente enteros porfa", usuario, sep=' ,')

dividendo = float(input("Escribe el dividendo: "))
divisor = float(input("Escribe el divisor: "))

print(dividendo/divisor)

print("-"*30)

edad = input("Se me olvido preguntar tu edad, q tan viejo sos?: ")
print(edad)






