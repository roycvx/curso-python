###
# 04 - Lista Métodos
# Los métodos más importantes para trabajar con listas
###

list1 = ['a', 'b', 'c', 'd']

# Añadir elementos de una lita

list1.append('e')
print(list1)

list1.insert(1, '@')
print(list1)

list1.extend(['😍', '😎'])
print(list1)

# Eliminar elementos de una lista
list1.remove('@')
print(list1)

valor_eliminado = list1.pop(1)
print(valor_eliminado, list1)

# Eliminar por lo bestia
del list1[-2]
print(list1)

# Eliminar todos los elementos de la lista
list1.clear()
print(list1)

# Eliminar rangos con del
list1 = ['🐼', '🐨', '🐷', '😾', '🐰']
del list1[1:3]
print(list1)

# Más métodos útiles

print("Ordenar listas")
numbers = [3, 4, 2, 8, 99, 101]
numbers.sort()
print(numbers)

# Creando un copia
print("Ordenar listas")
numbers = [3, 4, 2, 8, 99, 101]
sorted_numbers = sorted(numbers)
print(sorted_numbers)

# Ordenar listas de cadena de texto (todo minúsculas)
frutas = ['manzana', 'pera', 'limón', 'manzana', 'pera', 'limón']
sorted_frutas = sorted(frutas)
print(sorted_frutas)

# Ordenar listas de cadena de texto (mezclas de mayúsculas y minúsculas)
frutas = ['manzana', 'Pera', 'Limón', 'manzana', 'pera', 'limón']
sorted_frutas = sorted(frutas)
print(sorted_frutas)

frutas.sort(key=str.lower)
print(frutas)

# Más métodos útiles
animals = ['🐼', '🐨', '🐷', '😾', '🐰']
print(len(animals)) # --> 5
print(animals.count('🐷')) # --> 1
print('🐼' in animals) # True