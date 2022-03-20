# Sumar alturas de personas para sacar el promedio
# promedio es la suma de todos los valores en la lista y dividirlos entre el numero de valores

altura_estudiantes = input("Ingresa la altura de los estudiantes: ").split()
for n in range(0 , len(altura_estudiantes)):
    altura_estudiantes[n] = int(altura_estudiantes[n])
print(altura_estudiantes)

# suma de alturas o el total
altura_total = 0
for  altura in altura_estudiantes:
    altura_total = altura_total + altura # o también: altura_total += altura 
print("Promedio de alturas: " , altura_total)

# longitud de la lista
numero_de_estudiantes = 0
for estudiantes in altura_estudiantes:
    numero_de_estudiantes += 1
print("Numero de estudiantes: " , numero_de_estudiantes)

# promedio total de alturas
promedio_total = round(altura_total / numero_de_estudiantes)
print("Promedio Total: " , promedio_total)

