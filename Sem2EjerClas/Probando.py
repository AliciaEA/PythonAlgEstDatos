#Ciclos en Python, FOR

#Imprimir los numeros de 0 a 9
print("\nNumeros del 0 al 9")
for i in range(10):
    print(i, end='\t')


#Imprimir numeros pares del 2 al 100
print("\n\nNumeros pares del 2 al 100\n")
suma = 0
for i in range(2, 101):
    if i % 2 == 0:
        suma += i
        print(i, end='\t')
print("\n\nLa suma de los numeros pares es:", suma)


#Imprimir los numeros del 1 al 10
print("\n\nNumeros del 1 al 10\n")
for i in range(1, 11):
    print(i, end='\t')

#WHILE y ARREGLOS(listas)
nombres_con_j = ["Juan", "Jorge", "Javier", "Jairo", "Joaquin", "Julieta", "Julián", "Jesús", "Jesica", "Jazmín"]

buscar = input("\n\nIngrese el nombre a buscar que empiece con J: ")

for nombre in nombres_con_j:
    if nombre.upper() == buscar.upper():
        print("Nombre encontrado")
        break
else:
    print("No lo encontre beibi")

