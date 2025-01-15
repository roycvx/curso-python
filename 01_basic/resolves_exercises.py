###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

# Resueltos por @roycvx

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

### Completa aquí
print("Roy", "\nPanamá")

print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Completa aquí
print(f"\nEl tipo de dato de la variable {a} es: ", type(a))
print(f"El tipo de dato de la variable {b} es: ", type(b))
print(f"El tipo de dato de la variable {c} es: ", type(c))
print(f"El tipo de dato de la variable {d} es: ", type(d))
print(f"El tipo de dato de la variable {e} es: ", type(e))

print("--------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

### Completa aquí
str_int = int("12345")
print(str_int)
str_float = float(str_int)
print(str_float)
print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

### Completa aquí
name = "Roy"
age = "21"
height = 1.64
print(f"Hola! Me llamo {name} y tengo {age}, mido {height} metros")
print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

### Completa aquí
PI = 3.1416
round_number = round(PI)
result = round_number // 2

print("El resultado de este procedimiento es: ", result)

# EJERCICIOS ADICIONALES
print("\nEjercicio 6: Adicional")
print("\nPedir dos números y realizar operaciones matemáticas básicas")

### Completa aquí
first_number = float(input("Ingresa un número\n"))
second_number = float(input("Ingresa otro número\n"))

add = first_number + second_number
sub = first_number - second_number
mult = first_number * second_number
divi = first_number // second_number

print(f"La suma de {first_number} y {second_number} es: {add}")
print(f"La resta de {first_number} y {second_number} es: {sub}")
print(f"La multiplicación de {first_number} y {second_number} es: {mult}")
print(f"La división de {first_number} y {second_number} es: {divi}")

print("--------------")

print("\nEjercicio 7: Adicional")
print("Comprobar si un número es mayor, menor o igual a otro")
number1 = int(input("Ingrese un número: "))
number2 = int(input("Ingrese otro número: "))

if number1 > number2:
    print("El número mayor es ", number1)
elif number1 == number2:
    print(f"{number1} y {number2} son numeros iguales")
else:
    print("El número mayor es: ", number2)

print("--------------")