###
# 02 - Booleanos
# Valores lógicos: True (Verdadero) y False (Falso).
# Fundamentales para el control de flujo y la lógica en programación
###

# Los booleanos representan valores de verdad: True o False

print("\nValores booleanos básicos")
print("True")
print("False")

# Operadores de comparación: Devuelve un valor booleano.
print("\nOperadores de compración:")
print("5 > 3:", 5 > 3)     # True
print("5 < 3:", 5 < 3)      # False
print("5 == 5:", 5 == 5)    # True
print("5 != 3:", 5 != 3)    # True
print("5 >= 5:", 5 >= 5)    # True
print("5 <= 3:", 5 <= 3)    # False

print("\nComparación de cadenas:")
print("manzana < pera", "manzana" < "pera")
print("'Hola' == 'hola", 'Hola' == 'hola')

# Operadores lógicos: and, or, not
print("\nOperadores Lógicos: ")
print("True and True", True and True)    # True
print("True and False", True and False)  # False
print("True or False", True or False)    # True
print("False or True", False or True)    # True
print("not True", not True)              # False
print("not False", not False)            # True

#Ternarias
print("\nOperador ternario:")

edad = 17
print("Es mayor de fedad" if edad >= 18 else "Es menor de edad")