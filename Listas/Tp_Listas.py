import random

print('*'*120)
""" 1) Crear una lista con las notas de 10 estudiantes.
• Mostrar la lista completa.
• Calcular y mostrar el promedio.
• Indicar la nota más alta y la más baja.
 """
 
notas = [8, 9, 5, 4, 10, 5, 7, 3, 8, 7]
cantidad_notas = len(notas)

sumatoria = 0
for nota in notas:
    sumatoria += nota
promedio = sumatoria / cantidad_notas
print(f'El promedio de las notas es: {promedio}') 
print(f'La nota mas baja de la lista es: {min(notas)} ')
print(f'La nota mas alta de la lista es: {max(notas)} ')


print('*'*120) 
'''
2) Pedir al usuario que cargue 5 productos en una lista.
• Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
• Preguntar al usuario qué producto desea eliminar y actualizar la lista.
'''

productos = []
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
    print(producto)
    
    
print('*'*120) 
'''
3) Generar una lista con 15 números enteros al azar entre 1 y 100.
• Crear una lista con los pares y otra con los impares.
• Mostrar cuántos números tiene cada lista.'''


lista = []

while len(lista) != 15:
    numero_al_azar = random.randint(1, 100)
    lista.append(numero_al_azar)
    
pares = []    
impares = [] 

for num in lista:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)    
# Mostrar las listas
print("Lista original:", lista)
print("Números pares:", pares)
print("Números impares:", impares)

# Mostrar cuántos números tiene cada lista
print("Cantidad de números pares:", len(pares))
print("Cantidad de números impares:", len(impares))


print('*'*120) 
'''4) Dada una lista con valores repetidos:
• Crear una nueva lista sin elementos repetidos.
• Mostrar el resultado.'''

lista = [1, 3, 5, 3, 7, 1, 9, 5, 3]
lista_sin_repetidos = []

for el in lista:
    if el not in lista_sin_repetidos:
        lista_sin_repetidos.append(el)


# Mostrar el resultado
print("Lista original:", lista)
print("Lista sin repetidos:", lista_sin_repetidos)


print('*'*120) 
'''5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
• Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
• Mostrar la lista final actualizada.'''

lista_estudiantes = ['Juan Martin', 'Agustin', 'Victoria', 'Benjamin', 'Nicolas', 'Valentin', 'Marcela', 'Pedro']

respuesta = input('¿Quiere agregar un nuevo estudiante o eliminar uno existente? (agregar/eliminar): ').lower()
nombre = input('Ingrese el nombre por favor: ').strip()
nombre = nombre.capitalize()

if respuesta == 'eliminar':
    if nombre in lista_estudiantes:
        lista_estudiantes.remove(nombre)
        print(f"{nombre} ha sido eliminado.")
    else:
        print(f"{nombre} no está en la lista.")
elif respuesta == 'agregar':
    if nombre not in lista_estudiantes:
        lista_estudiantes.append(nombre)
        print(f"{nombre} ha sido agregado.")
    else:
        print(f"{nombre} ya está en la lista.")
else:
    print('La opción no es válida, por favor ingrese "agregar" o "eliminar".')

print(f'Lista actualizada: {lista_estudiantes}')
       
     
print('*'*120)        
'''6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el
último pasa a ser el primero).'''

lista = [1, 2, 3, 4, 5, 6, 7]

ultimo_elemento = lista.pop()  # Elimina y devuelve el último elemento
lista.insert(0, ultimo_elemento)  # Inserta ese elemento en la posición 0

print("Lista después de rotar:", lista)


print('*'*120) 
'''7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una
semana.
• Calcular el promedio de las mínimas y el de las máximas.
• Mostrar en qué día se registró la mayor amplitud térmica.'''

promedio_minimas = 0
promedio_maximas = 0

sum_minimas = 0
sum_maximas = 0

max_amplitud = 0
dia_maxima_amplitud = 0

temp_semanal = [
    [-5, 6],
    [-3, 9],
    [-1, 12],
    [1, 15],
    [3, 18],
    [-1, 10],
    [2, 5]
]

for i in range(len(temp_semanal)):
    minima, maxima = temp_semanal[i]
    sum_minimas += minima
    sum_maximas += maxima
    
    amplitud = maxima - minima
    if amplitud > max_amplitud:
        max_amplitud = amplitud
        dia_maxima_amplitud = i + 1
        
# Promedios
promedio_minimas = sum_minimas / len(temp_semanal)      
promedio_maximas = sum_maximas / len(temp_semanal)    


#Resultados
print(f"Promedio mínimas: {promedio_minimas:.2f}")
print(f"Promedio máximas: {promedio_maximas:.2f}")
print(f"El día con mayor amplitud térmica fue el día {dia_maxima_amplitud} con una amplitud de {max_amplitud}") 


print('*'*120) 
'''8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
• Mostrar el promedio de cada estudiante.
• Mostrar el promedio de cada materia.'''


# Lista con las notas de 5 estudiantes en 3 materias
notas = [
    [6, 10, 7],
    [5, 9, 10],
    [8, 8, 9],
    [9, 6, 7],
    [1, 10, 7]
]

# Sumas de las notas de cada estudiante
suma_estudiante1 = 0
suma_estudiante2 = 0
suma_estudiante3 = 0
suma_estudiante4 = 0
suma_estudiante5 = 0

# Recorrer la lista y sumar las notas de cada estudiante
# Calcula y mostrarmuestra el promedio de cada estudiante
for i in range(len(notas)):
    suma = notas[i][0] + notas[i][1] + notas[i][2]
    promedio = suma / 3
    print(f"Promedio del Estudiante {i+1}: {promedio:.1f}")

# Promedio por materia
num_estudiantes = len(notas)
num_materias = len(notas[0])

for materia in range(num_materias):
    suma_materia = 0
    for estudiante in range(num_estudiantes):
        suma_materia += notas[estudiante][materia]
    promedio_materia = suma_materia / num_estudiantes
    print(f"Promedio de la materia {materia + 1}: {promedio_materia:.1f}")


print('*'*120) 
'''9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
• Inicializarlo con guiones "-" representando casillas vacías.
• Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
• Mostrar el tablero después de cada jugada.'''

# Crear el tablero 3x3 con guiones "-"
tablero = [["-" for _ in range(3)] for _ in range(3)]

# Mostrar el tablero
print("Tablero inicial:")
for fila in tablero:
    print(" | ".join(fila))
print()

# Número de jugadas (por ejemplo, 4 jugadas)
for turno in range(1, 5):
    # Alternar jugador
    if turno % 2 == 1:
        ficha = "X"
    else:
        ficha = "O"

    print(f"Turno {turno} - Jugador con '{ficha}'")
    fila = int(input("Ingrese fila (0, 1, 2): "))
    columna = int(input("Ingrese columna (0, 1, 2): "))

    # Verificar si la casilla está vacía
    if tablero[fila][columna] == "-":
        tablero[fila][columna] = ficha
    else:
        print("¡Esa posición ya está ocupada! Intenta de nuevo.")
        # Repetir el turno actual
        turno -= 1
        continue

    # Mostrar el tablero actualizado
    for fila_actual in tablero:
        print(" | ".join(fila_actual))
    print()


print('*'*120) 
'''10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
• Mostrar el total vendido por cada producto.
• Mostrar el día con mayores ventas totales.
• Indicar cuál fue el producto más vendido en la semana.'''

# Matriz de ventas: 4 productos y 7 días
ventas = [
    [10, 12, 8, 15, 9, 11, 14], 
    [20, 18, 22, 19, 21, 20, 23], 
    [5, 7, 6, 8, 5, 7, 6],  
    [30, 28, 32, 29, 31, 30, 33]  
]

for i in range(4):
    total_producto = 0
    for j in range(7):
        total_producto += ventas[i][j]
    print(f"Total vendido del Producto {i+1}: {total_producto}")


# Primero sumamos las ventas de cada día
for dia in range(7):
    total_dia = 0
    for producto in range(4):
        total_dia += ventas[producto][dia]
    print(f"Ventas totales del Día {dia+1}: {total_dia}")

# Ahora buscamos el día con mayor venta total
max_ventas = 0
dia_max = 0
for dia in range(7):
    total_dia = 0
    for producto in range(4):
        total_dia += ventas[producto][dia]
    if total_dia > max_ventas:
        max_ventas = total_dia
        dia_max = dia + 1

print(f"El día con mayores ventas fue el Día {dia_max} con {max_ventas} ventas.")

# Sumamos las ventas de cada producto en toda la semana
sumas_productos = [0, 0, 0, 0]
for i in range(4):
    for j in range(7):
        sumas_productos[i] += ventas[i][j]

# Encontrar el producto con mayor venta
max_venta = sumas_productos[0]
producto_mas_vendido = 1
for i in range(1, 4):
    if sumas_productos[i] > max_venta:
        max_venta = sumas_productos[i]
        producto_mas_vendido = i + 1

print(f"El producto más vendido en la semana fue el Producto {producto_mas_vendido} con {max_venta} ventas.")
