import math

#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print('Hola Mundo!')

#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
#realizar la impresión por pantalla.

nombre = input('Ingrese su nombre: ')
saludo = print(f'Hola {nombre}')

#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#la impresión por pantalla.

nombre = input('Ingrese su nombre: ')
apellido = input('Ingrese su apellido: ')
edad = input('Ingrese su edad: ')
lugar_residencia = input('Ingrese su lugar de residencia: ')
print(f'Soy {nombre} {apellido}, tengo {edad} años, y vivo en {lugar_residencia}')

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
# su perímetro.

radio = int(input('Ingrese el radio del circulo: '))
area =  math.pi * radio ** 2
perimetro = 2 * math.pi * radio
print(f'El perimetro del circulo cuyo radio es {radio} es: {round(perimetro, 2)} y el area es {round(area, 2)}')

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale.

segundos = int(input('Ingrese la cantidad de segundos que se traducirá a horas: '))
horas = segundos / 3600
print(f'{segundos} segundos, equivalen a {horas} horas')

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número

numero = int(input('Ingrese un número: '))

print(f'''
      {numero} x 1 = {numero * 1}
      {numero} x 2 = {numero * 2}
      {numero} x 3 = {numero * 3}
      {numero} x 4 = {numero * 4}
      {numero} x 5 = {numero * 5}
      {numero} x 6 = {numero * 6}
      {numero} x 7 = {numero * 7}
      {numero} x 8 = {numero * 8}
      {numero} x 9 = {numero * 9}
      {numero} x 10 = {numero * 10}''')
      
#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.     

print('A continuación ingrese dos números diferentes de 0...')
num1 = int(input('Ingrese el primer número: '))
num2 = int(input('Ingrese el segundo número: '))
print(f''' 
      Suma: {num1 + num2},
      Resta: {num1 - num2},
      Multiplicación: {num1 * num2},
      División: {num1 / num2}''')  
      
#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
#modo:
#𝐼𝑀𝐶 = 𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔
#     (𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)2      

print('Bienvenido al programa para calcular Indice de masa corporal: ')
peso = float(input('Ingrese su peso: '))
altura = float(input('Ingrese su altura: '))

imc = peso / (altura ** 2)
print(f'Su indice de masa corporal es {imc}') 

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:

# 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9 . 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32
#                            5

celcius = float(input('Ingrese la temperatura en grados celsius: '))
farenheit = ((celcius * 9) / 5) + 32
print(f'{celcius} grados celsius equivalen a {farenheit} grados')

#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
#dichos números.

num1 = float(input('Ingrese el primer número: '))
num2 = float(input('Ingrese el segundo número: '))
num3 = float(input('Ingrese el tercer número: '))
promedio = (num1 + num2 + num3) / 3
print(f'El promedio de los 3 números que ingresó es: {promedio}')