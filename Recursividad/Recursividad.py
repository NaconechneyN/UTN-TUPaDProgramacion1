'''
1-Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
función para calcular y mostrar en pantalla el factorial de todos los números enteros
entre 1 y el número que indique el usuario
''' 
def factorial(numero):
    if numero == 0 or numero == 1:
        print(f'Resultado factorial parcial {numero} es: 1')
        return 1
    else:
        factorial_parcial = numero * factorial(numero - 1)
        print(f'Resultado factorial parcial {numero} es: {factorial_parcial}')
        return factorial_parcial

if __name__ == '__main__':
    numero = int(input('Ingrese el numero para calcular su factorial: '))
    resultado = factorial(numero)
    print(f'El factorial de {numero} es: {resultado}')
    
'''
2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
especifique.
'''        
""" def fibonacci(n):
    Función recursiva para calcular el valor de Fibonacci en la posición n.
    
    Reglas:
    - Si n es 0, retorna 0.
    - Si n es 1, retorna 1.
    - Para n > 1, retorna la suma de los dos anteriores (n-1) + (n-2).
    
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    print("--- Generador de Serie de Fibonacci (Recursivo) ---")
    
    while True:
        try:
            # Solicitamos la entrada del usuario
            entrada = input("\nIngrese la posición hasta la cual desea ver la serie (o 'salir' para terminar): ")
            
            # Opción de salida
            if entrada.lower() == 'salir':
                print("¡Hasta luego!")
                break

            n = int(entrada)
            
            if n < 0:
                print("Por favor, ingrese un número entero positivo.")
                continue

            print(f"\nCalculando la serie hasta la posición {n}...")
            print("-" * 30)
            
            # Lista para almacenar la serie completa
            serie = []
            
            # Iteramos desde 0 hasta n (inclusive)
            # Nota: Llamar a una función recursiva dentro de un bucle es computacionalmente
            # costoso para números grandes, pero cumple con el objetivo educativo.
            for i in range(n + 1):
                valor = fibonacci(i)
                serie.append(valor)
                # Opcional: Imprimir paso a paso
                # print(f"Posición {i}: {valor}")

            # Mostramos el resultado final
            print(f"Serie completa: {serie}")
            print(f"Valor en la posición {n}: {serie[-1]}")
            print("-" * 30)

        except ValueError:
            print("Error: Debe ingresar un número entero válido.") """

""" if __name__ == "__main__":
    main() """
    
'''
3) Crea una función recursiva que calcule la potencia de un número base elevado a un
exponente, utilizando la fórmula 𝑛
𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en unalgoritmo general.
'''   

""" def calcular_potencia(n, m):
    
    Calcula la potencia de un número de forma recursiva.
    
    Parámetros:
    n (int/float): La base.
    m (int): El exponente (debe ser un entero no negativo).
    
    Fórmula:
    n^m = n * n^(m-1)
    
    Caso Base:
    Cuando m es 0, el resultado es 1.
    
    # Caso base: cualquier número elevado a la 0 es 1
    if m == 0:
        return 1
    
    # Caso recursivo: n * potencia(n, m-1)
    else:
        return n * calcular_potencia(n, m - 1)

def main():
    print("--- Calculadora de Potencia (Recursiva) ---")
    print("Fórmula utilizada: n^m = n * n^(m-1)")
    
    while True:
        try:
            print("\nIngrese los datos (o escriba 'salir' en la base para terminar):")
            entrada_base = input("Base (n): ")
            
            if entrada_base.lower() == 'salir':
                break
                
            n = float(entrada_base)
            m = int(input("Exponente (m): "))
            
            # Validación para evitar recursión infinita con esta fórmula específica
            if m < 0:
                print("Error: Para esta fórmula básica, el exponente debe ser mayor o igual a 0.")
                continue
                
            # Llamada a la función recursiva
            resultado = calcular_potencia(n, m)
            
            print(f"\nResultado: {n} elevado a la {m} es: {resultado}")
            
            # Verificación (opcional) para demostrar que es correcto usando el operador nativo
            # print(f"Verificación Python (n**m): {n**m}")
            
        except ValueError:
            print("Error: Por favor ingrese números válidos.")
        except RecursionError:
            print("Error: El exponente es demasiado grande (límite de recursión excedido).")

if __name__ == "__main__":
    main() """
    
"""
4) Crear una función recursiva en Python que reciba un número entero positivo en base
decimal y devuelva su representación en binario como una cadena de texto.
Cuando representamos un número en binario, lo expresamos usando solamente ceros (0) y
unos (1), en base 2. Para convertir un número decimal a binario, se puede seguir este
procedimiento:
1. Dividir el número por 2.
2. Guardar el resto (0 o 1).
3. Repetir el proceso con el cociente hasta que llegue a 0.
4. Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario.    
Ejemplo: Convertir el número 10 a binario:
10 ÷ 2 = 5 resto: 0
5 ÷ 2 = 2 resto: 1
2 ÷ 2 = 1 resto: 0
1 ÷ 2 = 0 resto: 1
Leyendo los restos de abajo hacia arriba: 1 0 1 0 → El resultado binario es "1010".
"""

""" def decimal_a_binario_recursivo(n):
    
    #Convierte un número decimal entero positivo a binario de forma recursiva.
    
    #Lógica:
    #1. Caso Base: Si n < 2, el binario es simplemente el mismo número (0 o 1).
    #2. Caso Recursivo: Llamamos a la función con la división entera (n // 2)
    #   y al resultado le concatenamos el resto (n % 2) al final.
       
    #   Esto simula "leer los restos de abajo hacia arriba".
    
    if n < 0:
        return "El número debe ser positivo"
    elif n < 2:
        # Caso base: Si es 0 o 1, retornamos su valor como string
        return str(n)
    else:
        # Paso recursivo:
        # 1. Calculamos la parte binaria del cociente (n // 2)
        # 2. Le pegamos el resto (n % 2) a la derecha
        return decimal_a_binario_recursivo(n // 2) + str(n % 2)

def main():
    print("--- Conversor de Decimal a Binario (Recursivo) ---")
    
    while True:
        try:
            entrada = input("\nIngrese un número entero positivo (o 'salir'): ")
            
            if entrada.lower() == 'salir':
                break
            
            numero = int(entrada)
            
            if numero < 0:
                print("Por favor, ingrese un número positivo.")
                continue
                
            resultado = decimal_a_binario_recursivo(numero)
            
            print(f"Decimal: {numero}")
            print(f"Binario: {resultado}")
            
            # Verificación opcional usando la función nativa de Python bin()
            # Nota: bin() devuelve algo como '0b1010', por eso usamos [2:] para quitar el '0b'
            # print(f"Verificación Python: {bin(numero)[2:]}")

        except ValueError:
            print("Error: Debe ingresar un número entero válido.")

if __name__ == "__main__":
    main() """
    
'''
5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
lo es.
 Requisitos:
La solución debe ser recursiva.
No se debe usar [::-1] ni la función reversed().
'''    

""" def es_palindromo(palabra):

    #Función recursiva para determinar si una cadena es un palíndromo.
    
    #Un palíndromo se lee igual de izquierda a derecha que de derecha a izquierda.
    
    #Parámetros:
    #palabra (str): Cadena de texto a evaluar (sin espacios ni tildes).
    
    #Retorna:
    #bool: True si es un palíndromo, False en caso contrario.
   
    # 1. Caso Base 1: La palabra tiene 0 o 1 caracteres.
    # En ambos casos, es un palíndromo por definición.
    if len(palabra) <= 1:
        return True
    
    # 2. Caso Recursivo:
    # Comparamos el primer carácter con el último carácter.
    if palabra[0] == palabra[-1]:
        # Si son iguales, continuamos la recursión con la subcadena central.
        # palabra[1:-1] toma la cadena sin el primer y el último carácter.
        return es_palindromo(palabra[1:-1])
    else:
        # Si son diferentes, no es un palíndromo inmediatamente.
        return False

def main():
    print("--- Detector de Palíndromos Recursivo ---")
    print("La función opera sobre palabras sin espacios ni tildes.")
    
    while True:
        entrada = input("\nIngrese una palabra (o 'salir'): ").strip().lower()
        
        if entrada == 'salir':
            print("¡Gracias por usar el detector!")
            break
        
        # Opcional: Limpieza simple de la entrada para eliminar espacios
        palabra_limpia = "".join(entrada.split())
        
        if not palabra_limpia:
            print("Por favor, ingrese una palabra.")
            continue
        
        # Llamada a la función recursiva
        resultado = es_palindromo(palabra_limpia)
        
        if resultado:
            print(f"'{entrada}' SÍ es un palíndromo.")
        else:
            print(f"'{entrada}' NO es un palíndromo.")

if __name__ == "__main__":
    main()  """   
    
'''
6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
número entero positivo y devuelva la suma de todos sus dígitos.
 Restricciones:
No se puede convertir el número a string.
Usá operaciones matemáticas (%, //) y recursión.
Ejemplos:
suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
suma_digitos(9) → 9
suma_digitos(305) → 8 (3 + 0 + 5)

'''    
""" def suma_digitos(n):
   
    #Calcula la suma de los dígitos de un número entero positivo de forma recursiva,
    #sin convertir el número a string.
    
    #Lógica:
    #1. Obtener el último dígito con n % 10.
    #2. Eliminar el último dígito con n // 10.
    #3. Sumar el dígito obtenido al resultado de la llamada recursiva.
    
    #Parámetros:
    #n (int): El número entero positivo.
    
    #Retorna:
    #int: La suma total de sus dígitos.
    
    # 1. Caso Base: Si el número tiene un solo dígito (es menor que 10)
    if n < 10:
        return n
    
    # 2. Caso Recursivo:
    # a) n % 10: Obtiene el último dígito (el resto de la división por 10).
    # b) n // 10: Obtiene el resto del número (la división entera por 10).
    return (n % 10) + suma_digitos(n // 10)

def main():
    print("--- Sumador de Dígitos Recursivo ---")
    
    while True:
        try:
            entrada = input("\nIngrese un número entero positivo (o 'salir'): ")
            
            if entrada.lower() == 'salir':
                print("¡Programa finalizado!")
                break
            
            numero = int(entrada)
            
            if numero < 0:
                print("Error: Ingrese un número entero positivo.")
                continue
            
            # Llamada a la función recursiva
            resultado = suma_digitos(numero)
            
            print(f"El número ingresado es: {numero}")
            print(f"La suma de sus dígitos es: {resultado}")

        except ValueError:
            print("Error: Por favor, ingrese un número entero válido.")

if __name__ == "__main__":
    main() """
    
'''
7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
último nivel con un solo bloque.
Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
nivel más bajo y devuelva el total de bloques que necesita para construir toda la
pirámide.
 Ejemplos:
contar_bloques(1) → 1 (1)
contar_bloques(2) → 3 (2 + 1)
contar_bloques(4) → 10 (4 + 3 + 2 + 1)
'''    
""" def contar_bloques(n):
    
    #Calcula el número total de bloques necesarios para construir una pirámide
    #cuya base tiene 'n' bloques, reduciéndose en 1 por cada nivel hasta 1.
    
    #Parámetros:
    #n (int): Número de bloques en el nivel más bajo (entero positivo).
    
    #Retorna:
    #int: El número total de bloques.
    
    
    # 1. Validación (opcional pero recomendada para la recursión)
    if n < 0:
        # En el contexto del problema, un número negativo no tiene sentido.
        return 0
        
    # 2. Caso Base: Si el nivel es 0 o 1
    # Si n es 0, el total es 0.
    # Si n es 1, el total es 1.
    if n <= 1:
        return n
    
    # 3. Caso Recursivo:
    # El total es la suma de los bloques en el nivel actual (n)
    # más el total de bloques necesarios para construir el nivel superior (n-1).
    return n + contar_bloques(n - 1)

def main():
    print("--- Calculadora de Bloques de Pirámide Recursiva ---")
    print("La pirámide suma: n + (n-1) + ... + 1")
    
    while True:
        try:
            entrada = input("\nIngrese el número de bloques en la base (n) o 'salir': ")
            
            if entrada.lower() == 'salir':
                print("¡Programa finalizado!")
                break
            
            n = int(entrada)
            
            if n < 0:
                print("Error: El número de bloques en la base debe ser positivo.")
                continue
            
            # Llamada a la función recursiva
            resultado = contar_bloques(n)
            
            # Formatear la explicación de la suma (opcional para claridad)
            suma_explicita = " + ".join(str(i) for i in range(n, 0, -1))
            
            print(f"Número de niveles (base): {n}")
            print(f"Cálculo: {suma_explicita}")
            print(f"Total de bloques necesarios: {resultado}")

        except ValueError:
            print("Error: Por favor, ingrese un número entero válido.")

if __name__ == "__main__":
    main() """
    
'''
8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
aparece ese dígito dentro del número.
 Ejemplos:
contar_digito(12233421, 2) → 3
contar_digito(5555, 5) → 4
'''     
def contar_digito(numero, digito):
    
    #Función recursiva para contar cuántas veces aparece un dígito
    #específico en un número entero positivo.
    
    #Parámetros:
    #numero (int): El número entero positivo a analizar.
    #digito (int): El dígito (0-9) que se desea contar.
    
    #Retorna:
    #int: La cantidad de veces que el dígito aparece en el número.
    
    
    # 1. Caso Base: Si el número es 0, ya no hay más dígitos que contar.
    if numero == 0:
        return 0
    
    # 2. Paso Recursivo:
    
    # a) Obtener el último dígito del número
    ultimo_digito = numero % 10
    
    # b) Determinar si el último dígito coincide con el dígito buscado
    if ultimo_digito == digito:
        # Si coincide, sumamos 1 al resultado de la recursión
        contador_actual = 1
    else:
        # Si no coincide, sumamos 0
        contador_actual = 0
        
    # c) Llamada recursiva con el número sin el último dígito
    numero_restante = numero // 10
    
    # Retornamos el contador actual más el resultado de la llamada recursiva
    return contador_actual + contar_digito(numero_restante, digito)

def main():
    print("--- Contador de Dígitos Recursivo ---")
    
    while True:
        try:
            entrada_num = input("\nIngrese el número entero positivo (o 'salir'): ")
            
            if entrada_num.lower() == 'salir':
                print("¡Programa finalizado!")
                break
            
            numero = int(entrada_num)
            
            if numero < 0:
                print("Error: Ingrese un número entero positivo.")
                continue
            
            entrada_digito = input("Ingrese el dígito a buscar (0-9): ")
            digito = int(entrada_digito)
            
            if not (0 <= digito <= 9):
                print("Error: El dígito debe estar entre 0 y 9.")
                continue
            
            # Nota importante: Si el número es 0 y el dígito es 0, la respuesta es 1.
            # Nuestro caso base maneja n=0 devolviendo 0, pero el caso n=0, d=0 es especial.
            if numero == 0 and digito == 0:
                 resultado = 1
            else:
                 # Llamada a la función recursiva
                 resultado = contar_digito(numero, digito)
            
            print(f"El dígito {digito} aparece {resultado} veces en el número {numero}.")

        except ValueError:
            print("Error: Por favor, ingrese valores enteros válidos.")

if __name__ == "__main__":
    main()