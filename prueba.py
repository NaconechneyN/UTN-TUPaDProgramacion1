print('*** Saludos personalizados ***')
nombre = input('Ingrese su nombre: ')
print('Hola', nombre)


print('*** Suma de dos números ***')
num1 = int(input('Ingrese el primer número: '))
num2 = int(input('Ingrese el segundo valor: '))
suma = num1 + num2
print(f'La suma de los valores ingresados es: {suma}')

print('*** Perímetro del tríangulo ***')
lado1 = float(input('Ingrese el valor de un lado: '))
lado2 = float(input('Ingrese el valor de otro lado: '))
lado3 = float(input('Ingrese el valor del último lado: '))
perimetro = lado1 + lado2 + lado3

print(f'El Perímetro del triangulo según los datos enviados, es: {perimetro}')

price = float(input("Ingrese el precio del producto: "))
discount = float(input("Ingrese el descuento (%): "))
final_price = price - (price * discount / 100)
print("El precio con descuento es:", final_price)