'''
En base a una lista de valores se debe sacar el valor mas alto de la lista
'''
# se puede pedir los valores 
'''
puntajes_de_estudiantes = input("Digite los puntajes de los estudiantes: ").split()
for n in range(0, len(puntajes_de_estudiantes)):
    puntajes_de_estudiantes[n] = int(puntajes_de_estudiantes[n])
print(puntajes_de_estudiantes)
'''
# o directamente colocamos la lista de valores
puntajes_de_estudiantes = [78, 65, 89, 86, 55, 91, 64, 89]
# sacar el maximo valor de la lista
valor_maximo = 0
for valor in puntajes_de_estudiantes:
    if valor > valor_maximo:
        valor_maximo = valor
print(f"El valor maximo es: {valor_maximo}")