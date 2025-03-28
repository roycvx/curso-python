###
# EJERCICIOS (while)
###

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
print("\nEjercicio 1:")

num = 10
while num >= 1:
    print(num)
    num -= 1

# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
print("\nEjercicio 2:")
num = 1
sum = 0
while num <= 20:
    if num % 2 == 0:
        sum += num
    num += 1
print(sum)

# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
print("\nEjercicio 3:")

try:
    num = int(input("Ingresa un número entero positivo: "))
    
    fact = 1
    contador = 1
    while num > contador:
        fact *= (contador + 1)
        contador += 1

    print(fact)

except:
    print("Verifique que la entrada sea válida")

# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
print("\nEjercicio 4:")

try:
    password = input("Ingresa una contraseña: ")
  
    while len(password) < 8:

        print("La contraseña al menos debe tener 8 caracteres")
        password = input("Ingresa una contraseña: ")
    else:
        print("Contraseña válida")

except:
    print("Verifique que la entrada sea válida")

# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
print("\nEjercicio 5:")

try:
    num = int(input("Ingresa un número: "))
    contador = 1
    while contador <= 10:
        print(f"{num} * {contador} = {num * contador}")
        contador += 1
except:
    print("Verifique que la entrada sea válida")


# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.
print("\nEjercicio 6:") # TENGO QUE RESOLVER DE NUEVO, NO LO HICE SOLO 

try:
    num = int(input("Ingresa un número: "))

    """ 2, 3, 5, 7, 11, 13, 17, 19"""

    if num <= 1:
        print("Debes ingresar un número mayor a 1")
    else:

        contador = 2
        divisibles = 2
        divisores = 0

        while contador <= num:  
            
            while divisibles * divisibles <= contador:

                if contador % divisibles == 0:
                    divisores += 1
                    break

                divisibles += 1
            
            if divisores == 0:
                print(contador, "ES PRIMO")

            divisores = 0
            divisibles = 2
            contador += 1
except:
    print("Verifique que la entrada sea válida")