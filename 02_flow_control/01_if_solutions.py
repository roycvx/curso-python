###
# EJERCICOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

num1 = int(input("Ingrese un número entero: "))
num2 = int(input("Ingrese otro número entero: "))

if num1 > num2:
    print(f"El mayor es {num1}")
elif num1 == num2:
    print("Los números son iguales")
else:
    print(f"El mayor es {num2}")


# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)
#num1 = int(input("Ingrese un número entero: "))
#num2 = int(input("Ingrese otro número entero: "))

operation = input("Ingrese una operación (+, -, *, /): ")

if operation == '+':
    print(f"La suma de {num1} + {num2} = {num1 + num2}")
elif operation == '-':
    print(f"La resta de {num1} - {num2} = {num1 - num2}")
elif operation == '*':
    print(f"La multiplicación de {num1} * {num2} = {num1 * num2}")
elif operation == '/':
    if num2 == 0:
        print("No se puede divir por 0")
    else:
        print(f"La divisón de {num1} / {num2} = {num1 // num2}")
else:
    print("La operación que desea realizar no existe")

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

year = int(input("Introduce un año: "))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"El año {year} es bisiesto")
else:
    print(f"El año {year} no es bisiesto")

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

age = int(input("Introduce una edad: "))

if 0 <= age <= 2:
    print("Bebé")
if 3 <= age <= 12:
    print("Niño")
if 13 <= age <= 17:
    print("Adolescente")
if 18 <= age <= 64:
    print("Adulto")
if age >= 65:
    print("Adulto mayor")
else:
    print("Edad no válida")
