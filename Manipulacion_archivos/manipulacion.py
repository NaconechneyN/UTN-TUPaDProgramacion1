# --- Trabajo Practico de manipulación de archivos ---
FILE_TXT = 'productos.txt'
'''
1. Crear archivo inicial con productos: Crear un archivo de texto llamado 
productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad
'''

with open(FILE_TXT, 'w') as archivo:
    archivo.write('Mate, $150, 38\n')
    archivo.write('Bombilla, $60, 57\n')
    archivo.write('Matera, $300, 12')
    
'''
2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada 
línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente 
formato:
Producto: Lapicera | Precio: $120.5 | Cantidad: 30
'''    

with open(FILE_TXT, 'r') as a:
    print(f'--- Productos encontrados en {FILE_TXT}---')
    
    for linea in a:
        # --- Eliminamos espacios en blanco al inicio y final de la linea ---
        linea_limpia = linea.strip()
        
        # --- Omitir lineas vacías después del strip ---
        if not linea_limpia:
            continue
        
        # --- Dividir la línea usando la como como separador ---
        # --- Formato esperado : Nombre, Precio, Cantidad
        
        partes = linea_limpia.split(',')
        if len(partes) == 3:
            producto = partes[0].strip()
            precio = partes[1].strip()
            cantidad = partes[2].strip()
            
            # --- Mostrar el producto en el formato solicitado ---
            print(f'Prodcuto: {producto}| Precio: ${precio} | Cantidad: {cantidad}')
        
        else:
            # Mensaje de advertencia si la línea no tiene el formato correcto
            print(f"Advertencia: Línea con formato incorrecto (se ignorará): '{linea_limpia}'")

    print("--- Fin del listado de productos ---")
    
# nuevo producto
    
def validar_producto_no_vacio():
# --- Solicita y valida que se haya ingresado un producto
    while True:
        producto_ingresado = input('Ingrese un producto: ').strip().capitalize()
        if producto_ingresado:
            return producto_ingresado
        print("El producto no puede estar vacío. Intente de nuevo.")
    
# Validar cantidades ingresadas

def validar_cantidad():
# --- Solicita y valida que la cantidad sea un entero no negativo.
    while True:
        cantidad_str = input("Ingrese la cantidad de ejemplares (>= 0): ").strip()
        if not cantidad_str.isdigit():
            print("La cantidad debe ser un número entero no negativo. Intente de nuevo.")
            continue
        
        cantidad = int(cantidad_str)
        if cantidad >= 0:
            return cantidad
        else:
            print("La cantidad debe ser mayor o igual a cero. Intente de nuevo.")

# Validar el precio ingresado
            
def validar_precio():
    while True:
        precio_str = input('Ingrese el valor del producto, deber ser positivo: ').strip()
        try:
            # Convertimos cadena a flotante, si es posible.
            precio = float(precio_str)
            # Verificamos que el precio sea positivo
            if precio > 0:
                # Formateamos con dos decimales
                return f'${precio:.2f}'
            else:
                print('El precio debe ser un número posisitvo mayor que cero, Ingreselo nuevamente')
        except ValueError:
                print('Formato de precio inválido. Ingrese un número (Ej: 19.90 o 48): ')           
    
with open(FILE_TXT, 'a') as archivo:
    producto = validar_producto_no_vacio()
    precio = validar_precio()
    cantidad = validar_cantidad()
    
    archivo.write(f'\n{producto}, {precio}, {cantidad}')    
    
'''
4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en 
una lista llamada productos, donde cada elemento sea un diccionario con claves: 
nombre, precio, cantidad
'''    

with open(FILE_TXT, 'r') as a:
    lista_productos = []
    for linea in a:
        # --- Separo en partes usando la coma como delimitador
        partes = [p.strip() for p in linea.split(',')]
        
        # --- Nos aseguramos que tenga las 3 partes esperadas
        if len(partes) < 3:
            print(f'Advertencia: Linea incompleta detectada: {linea}. Salteada')
            continue # Saltea este producto
        nombre = partes[0]
        precio_str = partes[1]
        cantidad_str = partes[2] 
        
        # --- Limpieza y Conversión del Precio 
        precio_limpio = precio_str.replace('$', '').replace('Precio:', '').strip()
        
        try:
            precio = float(precio_limpio)
        except ValueError:
                print(f"Error: Precio inválido para {producto} ('{precio_str}'). Salteada.")
                continue # Saltea este producto
        
        # --- Conversion de la cantidad
        
        try:
            cantidad = int(cantidad_str)
        except ValueError:
            print(f'Error: Cantidad inválida para {producto} ({cantidad_str}). Salteando') 
            continue # Saltea este producto
        
        # --- Diccionario
        
        producto_dicc = {
            'nombre': nombre,
            'precio': precio,
            'cantidad': cantidad
        }  
        
        lista_productos.append(producto_dicc)        
        
        # --- Resultado
        print('--- Producto cargados: ---')
        print(lista_productos)    
        
'''
5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un 
producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si 
no existe, mostrar un mensaje de error.
'''     

def buscar_producto_por_nombre(lista_productos):

    busqueda = input('Ingrese el nombre del producto que desea encontrar: ').strip().capitalize()
    
    encontrado = False 
    
    for producto in lista_productos:
        if producto['nombre'].capitalize() == busqueda: 
            print("\n Producto encontrado:")
            print(f"  - Nombre: {producto['nombre']}")
            print(f"  - Precio: ${producto['precio']:.2f}")
            print(f"  - Cantidad: {producto['cantidad']} unidades")
            
            encontrado = True
            break 
    if not encontrado:
        print(f"\n Error: El producto '{busqueda}' no se encontró en el inventario.")

# --- 'lista_productos' ya deería existir
buscar_producto_por_nombre(lista_productos)

'''
6. Guardar los productos actualizados: Después de haber leído, buscado o agregado 
productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los 
productos actualizados desde la lista
'''

def guardar_productos(lista_productos, archivo_destino):
    try:
        with open(FILE_TXT, 'w') as a: # modo w para que se borre el contenido del archivo
            for producto in lista_productos:
                nombre = producto['nombre']
                precio = f'{producto['precio']:.2f}'
                cantidad = producto['cantidad']
                
                linea_a_escribir = f'{nombre}, {precio}, {cantidad}\n'
                
                a.write(linea_a_escribir)
        print(f"\n Archivo '{archivo_destino}' actualizado con {len(lista_productos)} productos.")
        
    except IOError as e:
        print(f"\n Error al intentar escribir en el archivo {archivo_destino}: {e}")            

# ---  variable FILE_TXT debería existir
guardar_productos(lista_productos, FILE_TXT)           