##
# 04 - Funciones
# Bloques de código reutilizables y parametrizables para hacer tareas específicas
##

""" Definición de una función
def nombre_de_la_funcion(parametro1, parametro2, ...):
    # docstring
    # cuerpo de la función
    # return valor_de_retorno # opcional

"""

# Ejemeplo de función de imprimir algo por consola

def saludar():
    print("¡Hola!")

saludar()

# Ejemplo de una función con parámetros

def saludar_a(nombre):
    print(f"¡Hola {nombre}!")


saludar_a("roy")
saludar_a("noemi")
saludar_a("manuel")
saludar_a("ross")

# Funciones con más parámetros
def suma(a, b):
    suma = a + b
    return suma

result = suma(2, 3)
print(result)

# Documentar las funciones con docstring
def restar(a, b):
    """Resta dos números y devuelve el resultado"""
    return a - b

# Parámetros por defecto
def multiplicar(a, b = 2):
    return a * b

print(multiplicar(2))

# Argumentos por posicion
def describir_persona(nombre, edad, sexo):
    print(f"Soy {nombre}, tengo {edad} y me identifico como {sexo}")

# Parametros son posicionales
describir_persona("roy", 28, "grande")
describir_persona("hombre", "carlo", 49)

# Argumentos por clave
# Parámetros nombrados
describir_persona(sexo="gato", nombre="roy", edad=24)
describir_persona(sexo="hombre", nombre="marcos", edad=44)

# Argumentos de longitud de variable (*args)
def sumar_numeros(*args):
    suma = 0
    for numero in args:
        suma += numero
    return suma

print(sumar_numeros(1,2,3,4,5))

# Argumentos de clave-valor variable (**kwargs)
def mostrar_informacion_de(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

print("\n")
mostrar_informacion_de(nombre="roy", edad=21, sexo="fiel")
print("\n")
mostrar_informacion_de(nombre="marcos", edad=40, country="Costa Rica")
print("\n")
mostrar_informacion_de(nombre="luis", es_sub=True, is_rich=True)
print("\n")
mostrar_informacion_de(nombre="PABLO", es_modo=True, gatos=True)