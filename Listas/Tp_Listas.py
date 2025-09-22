import random

""" 1) Crear una lista con las notas de 10 estudiantes.
• Mostrar la lista completa.
• Calcular y mostrar el promedio.
• Indicar la nota más alta y la más baja.
 """
 
""" notas = [8, 9, 5, 4, 10, 5, 7, 3, 8, 7]
cantidad_notas = len(notas)

sumatoria = 0
for nota in notas:
    sumatoria += nota
promedio = sumatoria / cantidad_notas
print(f'El promedio de las notas es: {promedio}') 
print(f'La nota mas baja de la lista es: {min(notas)} ')
print(f'La nota mas alta de la lista es: {max(notas)} ') """


'''
2) Pedir al usuario que cargue 5 productos en una lista.
• Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
• Preguntar al usuario qué producto desea eliminar y actualizar la lista.
'''

""" productos = []
for producto in range(5):
    producto = input('Ingrese un producto: ')
    productos.append(producto)
print()
# Mostramos la lista de productos ordenada alfabéticamente
productos_ordenados = sorted(productos)
print(f'Productos ordenandos alfabéticamente: {productos_ordenados}')
print()
producto_a_eliminar = input('¿Que producto desea eliminar?: ')
if producto_a_eliminar in productos:
    productos.remove(producto_a_eliminar)
    print(f'El prodcuto {producto_a_eliminar} ha sido eliminado de la lista')
else:
    print(f'EL producto {producto_a_eliminar} no se encuentra en la lista')
    
# Mostrar lista actualizada   
print('Lista actulizada: ') 
for producto in productos:
    print(producto) """

'''
3) Generar una lista con 15 números enteros al azar entre 1 y 100.
• Crear una lista con los pares y otra con los impares.
• Mostrar cuántos números tiene cada lista.'''


lista = []

while len(lista) != 15:
    numero_al_azar = random.randint(1, 100)
    lista.append(numero_al_azar)
 
# Mostrar las listas
print("Lista original:", lista)
print("Números pares:", pares)
print("Números impares:", impares)

# Mostrar cuántos números tiene cada lista
print("Cantidad de números pares:", len(pares))
print("Cantidad de números impares:", len(impares))

'''4) Dada una lista con valores repetidos:
• Crear una nueva lista sin elementos repetidos.
• Mostrar el resultado.'''

'''5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
• Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
• Mostrar la lista final actualizada.'''


'''6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el
último pasa a ser el primero).'''

'''7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una
semana.
• Calcular el promedio de las mínimas y el de las máximas.
• Mostrar en qué día se registró la mayor amplitud térmica.'''

'''8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
• Mostrar el promedio de cada estudiante.
• Mostrar el promedio de cada materia.'''

'''9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
• Inicializarlo con guiones "-" representando casillas vacías.
• Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
• Mostrar el tablero después de cada jugada.'''


'''10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
• Mostrar el total vendido por cada producto.
• Mostrar el día con mayores ventas totales.
• Indicar cuál fue el producto más vendido en la semana.'''