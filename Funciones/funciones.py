'''
1. Crear una función llamada imprimir_hola_mundo que imprima por
pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
programa principal.'''
import math


def imprimir_hola_mundo():
    print("!Hola Mundo!")
imprimir_hola_mundo()


'''
2. Crear una función llamada saludar_usuario(nombre) que reciba
como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. 
Llamar a esta función desde el programa
principal solicitando el nombre al usuario.
'''

def saludar_usuario(nombre):
    return f'hola, {nombre}'

if __name__ == '__main__':
    nombre_usuario = input('Ingrese su nombre: ')

    saludo = saludar_usuario(nombre_usuario)
    print(saludo)

'''3. Crear una función llamada informacion_personal(nombre, apellido,
edad, residencia) que reciba cuatro parámetros e imprima: informacion_personal(nombre, apellido,
edad, residencia). 
Pedir los datos al usuario y llamar a esta función con los valores ingresados.
'''
def informacion_personal(nombre, apellido, edad, residencia):
  print(f'''informacion_personal:
             Nombre: {nombre},
             Apellido: {apellido},
             Edad: {edad},
             Residencia: {residencia}''')


if __name__ == '__main__':
    print('Por favor ingresá tus datos personales: ')
    nombre = input('Ingrese su nombre: ')
    apellido = input('Ingrese su apellido: ')
    edad = int(input('Ingrese su edad: '))
    ciudad_residencia = input('Ingrese su ciudad de residencia: ')

    informacion_personal(nombre, apellido, edad, ciudad_residencia)

'''4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio 
    como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) 
    que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar 
    el radio al usuario y llamar ambas funciones para mostrar los resultados.'''

def calcular_area_circulo(radio):
    # formula del area de un circulo
    return math.pi * radio ** 2
def calcular_perimetro_circulo(radio):
    # formula del perímetro de un círculo
    return 2 * math.pi * radio

if __name__ == '__main__':
    r = float(input('Ingrese el radio: '))
    perimetro = calcular_perimetro_circulo(r)
    area = calcular_area_circulo(r)
    print(f'El perimetro del circulo de acuerdo al radio dado es: {perimetro}')
    print(f'El area del circulo de acuerdo al radio es: {area}')

'''5. Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes. Solicitar al usuario los segundos y mostrar el 
resultado usando esta función.'''

def segundos_a_horas(segundos):
    return segundos / 3600 # segundos que entran en una hora

if __name__ == '__main__':
    seg = float(input('Ingrese los segundos :'))
    horas = segundos_a_horas(seg)
    print(f'la cantidad de segundos ingresados: {seg}, equivale a {horas} horas')


'''6. Crear una función llamada tabla_multiplicar(numero) que reciba un
número como parámetro y imprima la tabla de multiplicar de ese
número del 1 al 10. Pedir al usuario el número y llamar a la función.'''

def tabla_multiplicar(numero):
     print(f'''
            #{numero} x 1 es :{numero * 1}
           # {numero} x 2 es :{numero * 2}
           # {numero} x 3 es :{numero * 3}
           # {numero} x 4 es :{numero * 4}
           # {numero} x 5 es :{numero * 5}
           # {numero} x 6 es :{numero * 6}
           # {numero} x 7 es :{numero * 7}
           # {numero} x 8 es :{numero * 8}
           # {numero} x 9 es :{numero * 9}
           # {numero} x 10 es :{numero * 10}''')

if __name__ == '__main__':
    n = int(input('Ingrese el numero del cual quiere consultar la tabla: '))
    tabla_multiplicar(n)


'''7. Crear una función llamada operaciones_basicas(a, b) que reciba
dos números como parámetros y devuelva una tupla con el resultado de sumarlos,
restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.'''

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b

    # División por cero
    if b != 0:
        division = a / b
    else:
        division = "Indefinida (División por cero)"

    return (suma, resta, multiplicacion, division)


if __name__ == "__main__":
    print("--- Calculadora de Operaciones Básicas ---")

    while True:
        try:
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))
            break
        except ValueError:
            print("Error: Por favor, introduce un número válido.")

    resultados = operaciones_basicas(num1, num2)

    # Asignar los elementos de la tupla a variables con nombres descriptivos
    res_suma, res_resta, res_multiplicacion, res_division = resultados

    print("\n--- Resultados ---")
    print(f"Número a: {num1}")
    print(f"Número b: {num2}")
    print("-" * 25)
    print(f"Suma (a + b):         {res_suma}")
    print(f"Resta (a - b):        {res_resta}")
    print(f"Multiplicación (a * b): {res_multiplicacion}")
    print(f"División (a / b):     {res_division}")
    print("-" * 25)


'''8. Crear una función llamada calcular_imc(peso, altura) que reciba el
peso en kilogramos y la altura en metros, y devuelva el índice de
masa corporal (IMC). Solicitar al usuario los datos y llamar a la función 
para mostrar el resultado con dos decimales.'''

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

if __name__ == '__main__':
    kg = float(input('Ingrese su peso en kg: '))
    mts = float(input('Ingrese su altura en mts: '))
    imc = calcular_imc(kg, mts)
    print(f'Su indice de masa corporal es: {imc}')


'''9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
una temperatura en grados Celsius y devuelva su equivalente en
Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
resultado usando la función.'''

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) +32
    return fahrenheit


if __name__ == '__main__':
    g_celsius = float(input('Ingrese la temperatura en grados celsius: '))
    g_fahrenheit = celsius_a_fahrenheit(g_celsius)

    print(f'EL equivalente en grados fahrenheit es: {g_fahrenheit}°F')


'''10.Crear una función llamada calcular_promedio(a, b, c) que reciba
tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta
función.'''

def calcular_promedio(a, b, c):
    return (a + b + c) / 3

if __name__ == '__main__':
    # Consideramos numeros decimales para evitar ese error
    num1 = float(input('Ingrese el primer numero: '))
    num2 = float(input('Ingrese el segundo numero: '))
    num3 = float(input('Ingrese el último numero: '))
    promedio = calcular_promedio(num1, num2, num3)

    print(f'El promedio de los números ingresados es: {promedio}')