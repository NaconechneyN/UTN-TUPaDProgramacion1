import random

#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

""" for n in range(0, 101):
    print(n)
 """

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.

""" numero = input('Ingrese su número: ')
digitos = 0
for d in numero:
    if d.isdigit():
        digitos += 1
print(digitos)
 """
#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

""" numero_1 = int(input('Ingrese el primer número:'))
numero_2 = int(input('Ingrese el segundo número: '))
sumatoria = 0

for n in range(numero_1 + 1, numero_2):
    sumatoria += n
print(sumatoria)    """ 


#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.

""" numero = int(input('Comienze a ingresar números:'))
total = 0
while numero != 0:
    total += numero
    numero = int(input('Ingrese el siguiente:'))
print(f'La suma de los numeros ingresados es: {total}')    
     """

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

""" numero = random.randint(0, 9)
numero_usuario = int(input('Ingrese el número que eligió: '))
contador = 0
while numero_usuario != numero: 
    numero_usuario = int(input('El número elegido es incorrecto, vuelva a intentar: '))
    contador += 1
print(f'Felicidades el número era el: {numero} y lo descubriste en {contador} intentos')   """  
    

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.

""" for n in range(100, -1, -2):
    print(n) """

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.

""" numero = int(input('Ingrese un número: '))
suma = 0
for n in range(numero+1):
    print(n)
    suma += n
print(f'la suma de los números comprendidos entre 0 y {numero} es: {suma}') """


#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).


""" pares = 0
impares = 0
positivos = 0
negativos = 0
cant_ingresada = 0
total = 100

while cant_ingresada < total: 
    numero = int(input('Ingrese un número: '))
    cant_ingresada += 1
    if numero < 0:
        negativos += 1
        if numero % 2 == 0: 
            pares += 1
        else:
            impares += 1            
    else:
        positivos += 1
        if numero % 2 == 0: 
            pares += 1
        else:
            impares += 1   
    
print(f'''Dentro de los número Ingresados tenemos: {negativos} negativos, {positivos} positivos,
      {pares} pares y {impares} impares''')     """            

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).
""" promedio = 0
cant_ingresada = 0
suma = 0
total = 3
while cant_ingresada < total: 
    numero = int(input('Ingrese un número: '))
    cant_ingresada += 1
    suma += numero
promedio = suma / cant_ingresada

print(f'El promedio de los numeros ingresados es {promedio}') """

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
# Solicitar al usuario el número
numero = input("Ingresa un número: ")

numero_invertido = ""
i = len(numero) - 1

# Usar un bucle while para recorrer el número desde el final
while i >= 0:
    numero_invertido += numero[i]
    i -= 1

print(f"El número invertido es: {numero_invertido}")