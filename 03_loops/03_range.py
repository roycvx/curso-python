##
# 03 - range()
# Permite crear una sencuencia de números. Puede ser útil para for, pero no solo para eso
##

print("range():")

nums = range(0,5) # No crea una lista
print(nums)

# Genera una sencuencia de números del 0 al 9
for num in range(10):
    print(num)

# range(inicio, fin)
for num in range(0, 10, 2):
    print(num)

# Negativos
for num in range(10, 0, -1):
    print(num)


nums = range(10)
list_of_nums = list(nums)
print(list_of_nums)

# Seria para hacerlo cinco veces

contador = 0
while contador < 5:
    print("Cinco veces algo")
    contador += 1

# Seria para hacerlo cinco veces
for _ in range(5):
    print("Hacer cinco veces algo")