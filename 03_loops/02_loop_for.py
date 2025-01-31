##
# 02 - Bucles (for)
# Permiten ejecutar un bloque de código repetidamente mientras ITERA un iterable o una lista
##

print("Bucle For:")

# Iterar una lista

frutas = ["manzana", "pera", "mandarina"]
for fruta in frutas:
    print(fruta)

# Iterar sobre cualquier cosa que sea iterable
cadena = "roy"
for caracter in cadena:
    print(caracter)

# enumerate()
frutas = ["manzana", "pera", "mandarina"]
for index, fruta in enumerate(frutas):
    print(f"El índice es {index} y la fruta es {fruta}")

# Bucles anidados
letras = ['a', 'b', 'c']
numeros = [1, 2, 3]

for letra in letras:
    for numero in numeros:
        print(f"{letra} x {numero} = {letra * numero}")

# break
print("Break:")
animales = ["perro", "gato", "raton", "loro", "pez", "canario"]

for animal in animales:
    print(animal)
    if animal == 'loro':
        break

#continue
print("\nContinue:")

animales = ["perro", "gato", "raton", "loro", "pez", "canario"]

for animal in animales:
    if animal == 'loro':
        continue
    print(animal)

# Compresión de las listas (list comprehension)
animales = ["perro", "gato", "raton", "loro", "pez", "canario"]
animales_mayusculas = [animal.upper() for animal in animales]
print(animales_mayusculas)

# Muestra los números pares de una lista
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [num for num in numeros if num % 2 == 0]
print(pares)
