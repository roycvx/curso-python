###
# 01 - Bucles (while)
# Permiten ejecutar un bloque de código repetidamente mientras se cumple una condición
###

print("Bucle While:")

# Bucle con una simple condición

contador = 0

while contador < 5:
    print(contador)
    contador += 1 # Incrementamos para evitar un bucle infinito

# Utilizando la palabra break, para romper el bucle
print("Bucle while con break:")
contador = 0

while True:
    print(contador)
    contador += 1

    if contador == 5:
        break # Sale del bucle

# Utilizando continue
# continue lo que hace es saltar esa iteración en concreto y
# continuar con el bucle.
print("Bucle con continue: ")

contador = 0

while contador < 10:
    contador += 1

    if contador % 2 == 0:
        continue
    # Este código no se ejecuta
    print(contador)

# Else
print("Bucle while con else: ")

contador = 0

while contador < 5:
    contador += 1
    print(contador)
else:
    print("El bucle ha terminado")

# Pedirle a un usuario un número positivo si no, no lo dejamos en paz

numero = -1
while numero < 0:
    try:
        numero = int(input("Escribe un número positivo: "))
        if numero < 0:
            print("El número deber ser positivo")

    except:
        print("Deber introducir un número")
