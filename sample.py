'''def repetir_nombre(nombre, veces):
    for _ in range(veces):
        print(nombre + " crack")

# Pedir al usuario su nombre y el número

nombre = input("Ingrese su nombre: ")
numero = int(input("Ingrese un número: "))

# Llamar a la función para repetir el nombre
repetir_nombre(nombre, numero)
'''

import math

area = int(input("What square root do you need?: "))

squareroot = math.sqrt(area)

print(f"La raiz cuadrada de {area} es {squareroot:.0f}")