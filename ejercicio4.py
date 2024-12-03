# variables
suma_total_notas = 0 
numero_notas = 0 
nota = input("Ingresa una nota o escribe 'fin' para terminar: ")


# Bucle para ingresar notas hasta que se escriba 'fin' 
while nota != 'fin': 
    suma_total_notas += float(nota) # Transformar notas en numeros decimales
    numero_notas += 1 # Agrega la variable del lado derecho (1), a la variable numero_notas que era 0
    nota = input("Ingresa una nota o escribe 'fin' para terminar: ") # Repetir el input para que siga el bucle hasta que diga la palabra fin

# Calcular el promedio de las notas ingresadas
if numero_notas > 0: # Si el numero_notas es mayor que 0, entonces el promedio sera la suma de notas / en la cantidad de notas
    promedio = suma_total_notas / numero_notas 
    
    
# Determinar si el usuario aprueba o reprueba 

if promedio >= 4.0: # Si el promedio es mayor o igual a 4.0, entonces el alumno aprobo
    resultado = "Aprobaste"
else: # Si es distinto, entonces es reprobado
    resultado = "!Reprobaste!" 

print(f"El promedio es: {promedio}") #imprimo el resultado del if. la f es para la cadena, para que me figure el texto y el resultado.  
print(resultado) # imprimo el resultado si es distinto al if

