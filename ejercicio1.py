# Variables
n = int(input("Introduce un número: "))


lista = []
contador = 1

# Bucle para generar la lista
while contador <= n:
    lista.append(contador)
    contador += 1


print("lista de numeros", lista)

# Bucle para la suma total de los valores de la lista
suma_total = 0

for listas in lista:
    suma_total += listas
print(suma_total)    


# Variable para generar nueva lista
nueva_lista = []

# Asignacion de numeros pares a la nueva lista
for pares in lista:
     if pares % 2 == 0:
        nueva_lista.append(pares) 
print("la nueva lista es: ", nueva_lista)   