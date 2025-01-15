###
# 04 - variables
# Las variables sirven para guardar datos en memoria.
# Python es un lenguaje de tipado dinámico y de tipado fuerte.
###

# Asignar una variable
# solo hace falta poner esto

my_name = "roy"

# print(my_name)

# age = 22
# print(age)

age = 21
# print(age)

# Tipado dinámico: el tipo de dato se determina dinámicamente en tiempo de ejecución
# que no tienes que declararlo explicitamente.

name = "roy"
print(type(name))

name = 32
print(type(name))

#Tipado fuerte: Python no realiza conversiones de tipo automático.

# print(10 + "2")
# f-string (literal de cadena de formato)
# desde la version 3.6
print(f"Hola {my_name}, tengo {age} años")

# No recomendada forma de asignar variables
name, age, city = "roy", 21, "Panama"

# Convenciones de nombres de variables
mi_nombre_de_variable = "ok" # snake_case
nombre = "ok"

miNombreDeVariable = "no recomendado" # camelCase
MiNombreDeVariable = "no recomendado" # PascalCase
minombredevariable = "no recomendado" # todojunto

mi_nombre_de_variable_123 = "ok"

MI_CONSTANTE = 3.14 # UPPER_CASE -> constantes

# Nombres no válidos de variables
# 1213131_variable
# mi-variable = "ok"
# mi variable = "ok"

# print(help('keywords'))

is_user_logged_in: bool = True
print(is_user_logged_in)

is_user_logged_in = 42
print(is_user_logged_in)
