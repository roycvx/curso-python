###
# 01 - Sentencias condicionales (if, elif, else)
# Permiten ejecutar bloques de código solo si se cumplen ciertas condiciones
###

import os

os.system("clear")

print("\nSentencia simple condicional")

edad = 18

if edad >= 18:
    print("Eres mayor de edad")
    print("Felicidades")


edad = 15

if edad >= 18:
    print("Eres mayor de edad")
    print("Felicidades")

print("\nSentencia condicional else")

edad = 15

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

print("\nSentencia con elif")

nota = 9
if nota >= 9:
    print("!Sobresaliente¡")
elif nota >= 7:
    print("¡Notable!")
elif nota >= 5:
    print("¡Aprobado!")
else:
    print("¡No está calificado!")

print("Condiciones múltiples")

edad = 15
tiene_carnet = False

if edad >= 18 and tiene_carnet:
    print("Puedes conducir")
else:
    print("¡Policía!")

# Estas en otro pueblo
if edad >= 18 or tiene_carnet:
    print("Puedes conducir")
else:
    print("Paga al policía y te deja de conducir !!!")

es_fin_de_semana = False

if not es_fin_de_semana:
    print("Hay que estudiar")

print("\nAnidar condicionales")

edad = 20
tiene_dinero = True

if edad >= 18:
    if tiene_dinero:
        print("Puedes ir a la discoteca")
    else:
        print("Quédate en casa")
else:
    print("No puedes entrar a la disco")

# Más fácil
if edad < 18:
    print("No puedes entrar en la disco")
elif tiene_dinero:
    print("Puedes ir a la disco")
else:
    print("Quédate en casa")