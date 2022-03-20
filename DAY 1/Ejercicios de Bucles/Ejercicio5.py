total = 0
for numero in range(2, 101, 2):
    total += numero
print(total)

# otra forma seria:
total2 = 0
for numero in range(1, 101):
    if numero % 2 == 0:
        total2 += numero
print(total2)