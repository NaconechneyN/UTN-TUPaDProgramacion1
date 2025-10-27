'''
1) Dado el diccionario precios_frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}
Añadir las siguientes frutas con sus respectivos precios:
● Naranja = 1200
● Manzana = 1500
● Pera = 2300
'''

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzanaa'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas) 

'''
2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
● Banana = 1330
● Manzana = 1700
● Melón = 2800
'''

precios_frutas['Banana'] = 1330
precios_frutas['Manzanaa'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

'''
3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
precios.
'''

lista_frutas = list(precios_frutas.keys())
print(lista_frutas)

'''
4) Escribí un programa que permita almacenar y consultar números telefónicos.
• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
• Luego, pedí un nombre y mostrale el número asociado, si existe.
'''


#Inicializar la agenda (diccionario)
agenda_contactos = dict()
MAX_CONTACTOS = 5
print("--- AGENDA TELEFÓNICA ---")

# ---CARGA DE CONTACTOS---
for i in range(MAX_CONTACTOS):
    print(f"\nCargando Contacto {i + 1} de {MAX_CONTACTOS}:")

    # A. VALIDACIÓN Y OBTENCIÓN DEL NOMBRE
    while True:
        nombre_input = input("   - Ingresa el nombre: ").strip()

        if not nombre_input:
            print(" Error: El nombre no puede estar vacío.")
            continue
        
        # Validar solo letras y espacios (y aceptar que no esté duplicado si quieres)
        if not nombre_input.replace(' ', '').isalpha():
            print("Error: El nombre solo debe contener letras y espacios.")
            continue
            
        nombre_contacto = nombre_input.title()
        break # Nombre es válido

    # B. VALIDACIÓN Y OBTENCIÓN DEL TELÉFONO
    while True:
        telefono_input = input(" Ingresa el número de teléfono (solo dígitos): ").strip()

        if not telefono_input:
            print(" Error: El teléfono no puede estar vacío.")
            continue

        # Validar solo dígitos
        if not telefono_input.isdigit():
            print(" Error: El número solo debe contener dígitos (0-9).")
            continue
            
        telefono_contacto = telefono_input
        break # Teléfono es válido

    # C. ALMACENAR EN EL DICCIONARIO
    # El nombre es la CLAVE y el teléfono es el VALOR
    agenda_contactos[nombre_contacto] = telefono_contacto
    print(f"Contacto '{nombre_contacto}' guardado con éxito.")


# --- PARTE 2: CONSULTA DE CONTACTOS ---
print("\n" + "="*40)
print("--- CONSULTA DE NÚMEROS ---")

# Pedir al usuario el nombre a buscar
nombre_a_buscar = input("Ingresa el nombre del contacto que deseas buscar: ").strip().title()

# Consultar en el diccionario
if nombre_a_buscar in agenda_contactos:
    # Si el nombre existe como clave en el diccionario
    numero = agenda_contactos[nombre_a_buscar]
    print(f"\nEl número de teléfono para **{nombre_a_buscar}** es: **{numero}**")
else:
    # Si el nombre no es una clave
    print(f"\nLo siento, el contacto **{nombre_a_buscar}** no se encontró en la agenda.")

print("\n--- PROGRAMA FINALIZADO ---")

'''
5) Solicita al usuario una frase e imprime:
• Las palabras únicas (usando un set).
• Un diccionario con la cantidad de veces que aparece cada palabra.
'''

frase = input('Ingrese su frase: ')

palabras_separadas = frase.split()
palabras_unicas = set(palabras_separadas)
recuento = {}
for palabra in palabras_separadas:
    recuento[palabra] = recuento.get(palabra, 0) + 1   

print(f'''
      Palabra unicas: {palabras_unicas}
      Recuento: {recuento}
      ''')
      
'''
6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
Luego, mostrá el promedio de cada alumno.
'''      
alumnos = {}
cantidad_alumnos = 3
cantidad_notas = 3
for i in range(cantidad_alumnos):
    nombre = input(f'\n--- ALUMNO {i + 1} ---\nIngrese el nombre del alumno: ')
    notas = []
    for j in range(cantidad_notas):
        nota = float(input(f'Ingrese la nota {j + 1}: ')) 
        notas.append(nota)
    
    tupla_notas = tuple(notas)
        
    # Asignacion al diccionario
    alumnos[nombre] = tupla_notas
    
print("\n" + "="*90)
print("Datos cargados:", alumnos)
print("="*90)

# Cálculo y Muestra del Promedio
print("\n--- PROMEDIO DE CADA ALUMNO ---")

# Iterar sobre las claves y valores (nombre y tupla_notas) del diccionario
for nombre, tupla_notas in alumnos.items():
    # 1. Calcular la suma de las notas
    suma_notas = sum(tupla_notas)
    
    # 2. Calcular el promedio
    promedio = suma_notas / len(tupla_notas)
    
    # 3. Mostrar el resultado
    print(f'El promedio de {nombre} es: {promedio:.2f}') # .2f para mostrar 2 decimales 
    
    
''' 
7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
y Parcial 2:
• Mostrá los que aprobaron ambos parciales.
• Mostrá los que aprobaron solo uno de los dos.
• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).
'''

aprobados_parcial1 = {101, 105, 110, 112, 115, 120, 125, 130}
aprobados_parcial2 = {101, 102, 110, 115, 122, 125, 135}

aprobaron_ambos = aprobados_parcial1 & aprobados_parcial2 
print(f'Los alumnos que aprobaron ambos parciales: {aprobaron_ambos}')
aprobaron_uno_de_dos = aprobados_parcial1 ^ aprobados_parcial2
print(f'Los alumnos que aprobaron uno de los dos: {aprobaron_uno_de_dos}')
al_menos_uno = aprobados_parcial1 | aprobados_parcial2 
print(f'Y los alumnos que aprobaron al menos uno: {al_menos_uno}')

'''
8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
Permití al usuario:
• Consultar el stock de un producto ingresado.
• Agregar unidades al stock si el producto ya existe.
• Agregar un nuevo producto si no existe
'''   

stock = dict()

stock['Computadoras'] = 156
stock['Tablets'] = 312
stock['Celulares'] = 586

# Consulta de un producto:
print(f'La cantidad de celulares disponibles es: {stock['Celulares']}')

# Agregar Unidades si ya existe el producto:
print(f'La nueva cantidad de Computadoras es: {stock['Computadoras']+ 22}')

# Agregar producto que no existe en stock
stock['Relojes'] = 423
print(stock)


#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos
#   Permití consultar qué actividad hay en cierto día y hora.

agenda = {
    ('Lunes', 9): 'Reunión de planificación de sprint',
    ('Lunes', 14): 'Clase de Python avanzada',
    ('Martes', 11): 'Entrenamiento en gimnasio',
    ('Miércoles', 10): 'Llamada con cliente A',
    ('Jueves', 15): 'Preparación de informe trimestral',
    ('Viernes', 18): 'Cena con amigos'
}

print("--- Mi Agenda Semanal Creada ---")
print(agenda)

# ----------------------------------------------------
# 2. Función para Consultar la Actividad
# ----------------------------------------------------
def consultar_evento(dia, hora):
    clave_consulta = (dia.capitalize(), hora)
    evento = agenda.get(clave_consulta, f"No hay eventos programados para {dia} a las {hora}hs.")
    return evento

# ----------------------------------------------------
# 3. Interfaz de Consulta para el Usuario
# ----------------------------------------------------

print("\n--- Consultar Evento ---")

try:
    # Solicitar datos al usuario
    dia_consulta = input("Introduce el día que quieres consultar (ej: Lunes, Martes): ").strip()
    hora_consulta = int(input("Introduce la hora que quieres consultar (ej: 9, 14, 18): ").strip())
    
    # Realizar la consulta
    resultado = consultar_evento(dia_consulta, hora_consulta)
    
    # Imprimir el resultado
    print(f"\n[Consulta: {dia_consulta.capitalize()} a las {hora_consulta}hs]")
    print(f"ACTIVIDAD: {resultado}")
    
except ValueError:
    print("\nError: Por favor, introduce un número válido para la hora.")
    
    
'''
10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
diccionario donde:
• Las capitales sean las claves.
• Los países sean los valores.
'''    

paises_capitales = {
    'Argentina': 'Buenos Aires',
    'Chile': 'Santiago',
    'España': 'Madrid',
    'México': 'Ciudad de México',
    'Canadá': 'Ottawa'
}

capitales_paises = {}

for pais, capital in paises_capitales.items():
    capitales_paises[capital] = pais
    
print('---Diccionario Original (País: Capital): ---')
print(paises_capitales)

print('\n---Diccionario invertido (Capital: País) ---')
print(capitales_paises)
    