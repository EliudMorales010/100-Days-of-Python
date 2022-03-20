# Generador de Contraseñas
# Preguntar:
'''
Cuantas letras quiere en su contraseña?
Cuantos simbolos quiere en su contraseña?
Cuantos numeros quiere en su contraseña?

'''
from asyncio.windows_events import NULL
import random
import secrets
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
        's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 
        'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print(' --- Bienvenidos a el Generador de Contraseñas! --- ')

nLetras = int(input('Cuantas letras quiere para su contraseña?\n'))
nSimbolos = int(input('Cuantos simbolos quiere para su contraseña?\n'))
nNumeros = int(input('Cuantos numeros quiere para su contraseña?\n'))

'''
# Nivel facil
# utilizo el modulo random para obtener un elemento aleatorio
contraseña = ""
for caracter in range(1, nLetras + 1):
        # 1 al 4
        caracter_aleatorio = random.choice(letras)
        contraseña = contraseña + caracter_aleatorio
        # o así: contraseña += random.choice(letras)

for caracter in range(1, nSimbolos + 1):
        contraseña += random.choice(simbolos)

for caracter in range(1, nNumeros + 1):
        contraseña += random.choice(numeros)

print(contraseña)
'''

# Nivel Dificil
lista_de_contraseña = []
for caracter in range(1, nLetras + 1):
        lista_de_contraseña.append(random.choice(letras))

for caracter in range(1, nSimbolos + 1):
        lista_de_contraseña.append(random.choice(simbolos))

for caracter in range(1, nNumeros + 1):
        lista_de_contraseña.append(random.choice(numeros))

print(lista_de_contraseña)
random.shuffle(lista_de_contraseña)
print(lista_de_contraseña)

# convertir una lista a una cadena(string)
contraseña = ""
for caracter in lista_de_contraseña:
        contraseña = contraseña + caracter
print(f"Tu contraseña es: {contraseña} ")
