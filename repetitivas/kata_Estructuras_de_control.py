#Ejercicio 1: Bucle for para números pares
for n in range(2, 21, 2): # Si cambiamos el primer 2 dentro de la funcion range por un 1, imprimimos impares
    print(n)              # Si fuera con paso tres imprimiría 2, 5, 8, 11, 14, 17 y 20   
    

#Ejercicio 2: Bucle while con suma acumulativa    

suma = 0
print('Ingresa número hasta llegar a 100, luego de eso se detendrá')
while suma < 100: # Si el primer numero ingresado es mayor a cien, imprimimos la suma
    try: # Para evitar el fallo del programa, si se ingresa una letra colocamos la instruccion dentro de un blocke try except
        numero = int(input('Ingrese un número: '))
        suma += numero
            
    except ValueError:
        print(f'El caracter ingresado no es válido, intenta nuevamente')        
print(f'La suma total es {suma}') 


#Ejercicio 3: Filtrar palabras por letra inicial

frutas = ["apple", "banana", "avocado"]

for f in frutas:
    if f.lower().startswith('a'):# Para que se impriman las que comienzan con A o a usaría lower() primero
        print(f)
        
        
#Ejercicio 4: Tabla de multiplicar del 7

multiplicadores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
# Podriamos pedirle al usuario que ingrese el n°
tabla_numero = int(input('Ingrese el número del cual quiere imprimir la tabla: ')) 
# Podriamos almacenar los resultados en una lista
resultados = [] 

for n in multiplicadores:
    resultado = n * tabla_numero
    resultados.append(resultado)
    print(f'{tabla_numero} x {n} = {resultado}')
    print(resultados)
    
#Ejercicio 5: Contador de vocales    

texto = input('Ingrese su palabra o frase: ')
vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ" # Para contar las vocales con acento las agregaría dentro de la variable 
cantidad_vocales = 0
for letra in texto:
    if letra in vocales:
        cantidad_vocales += 1
print(cantidad_vocales)

 
#Ejercicio 6: Números repetidos en una lista
lista = [3, 1, 3, 5, 1]
duplicados = []

for i in range(len(lista)):
    if lista.count(lista[i]) > 1 and lista[i] not in duplicados:
        duplicados.append(lista[i])    
        
print(duplicados) 
    
     
# Ejercicio 7: FizzBuzz      

for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0: # 1° debemos evaluar la doble porque si ingresa a otra condicion nunca va a evaluar 
        print('FizzBuzz')
    elif n % 3 == 0:
        print('Fizz')   # Para extender el juego deberiamos contemplar todas las combinaciones
    elif  n % 5 == 0:
        print('Buzz') 
        
# Ejercicio 8: Frecuencia de palabras  
cadena = "hola hola mundo"
frecuencia = {}
# Separamos cadena en palabras
palabras = cadena.split()
# Una opcion para eliminar las comas sería utilizando el metodo replace(',', '')
for palabra in palabras:
    if palabra in frecuencia:
        frecuencia[palabra] += 1
    else:
        frecuencia[palabra] = 1

print(frecuencia)        
      
       
#Ejercicio 9: Filtrar consonantes       

cadena = "Hola"
cadena_lower = cadena.lower()  # Maneja mayúsculas y minúsculas

consonantes = "bcdfghjklmnpqrstvwxyz"
nueva_cadena = ""

for caracter in cadena_lower:
    if caracter in consonantes:
        nueva_cadena += caracter

print(nueva_cadena)  


#Ejercicio 10: Números primos

numero = int(input('o un número entero positivo: '))
for num in range(2, numero + 1):
    es_primo = True
    for divisor in range(2, int(num ** 0.5) + 1): #  la verificación sea mucho más rápida.
        if num % divisor == 0:
            es_primo = False
            break
    if es_primo:
        print(num)
        
        
'''
Diagrama de flujo ejercicio 4 

for n in multiplicadores:
    resultado = n * tabla_numero
    resultados.append(resultado)
    print(f'{tabla_numero} x {n} = {resultado}')
    print(resultados)
    
    
[Inicio]
     |
     v
[Solicitar número]  <--- Usuario ingresa `n`
     |
     v
[Crear lista vacía `resultados`]
     |
     v
[Para cada `n` en multiplicadores (1 a 10)]
     |
     v
[Calcular `resultado = n * tabla_numero`]
     |
     v
[Agregar `resultado` a `resultados`]
     |
     v
[Imprimir `tabla_numero x n = resultado`]
     |
     v
[Imprimir `resultados`]
     |
     v
[Fin del ciclo]
     |
     v
   [Fin]

'''        

# Modificacmos el ejercicio 7 para usar break y continue

for n in range(1, 101):
    if n == 13:
        continue  # Salta el número 13 y pasa a la siguiente iteración
    if n % 3 == 0 and n % 5 == 0:
        print('FizzBuzz')
    elif n % 3 == 0:
        print('Fizz')
    elif n % 5 == 0:
        print('Buzz')
        
print('****************************************************************************************************')  

for n in range(1, 101):
    if n == 50:
        break  # Finaliza el ciclo cuando n llegue a 50
    if n % 7 == 0:
        print(f"Se encontró un número divisible por 7: {n}")
        break  # Sale del ciclo si encuentras un número que cumple
    if n % 3 == 0 and n % 5 == 0:
        print('FizzBuzz')
    elif n % 3 == 0:
        print('Fizz')
    elif n % 5 == 0:
        print('Buzz')      