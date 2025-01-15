# #Boxes by Joaquin Leiva

# import math
from colorama import *
init()
# number_items = int(input("Insert the number of items: ")) # Asking for the number of items
# print(" ") #Spacing
# items_per_box = int(input("How many items you'd like to pack in each box?: ")) # Asking for the number of items per box

# #Function 

# def itemsinbox(number_items, items_per_box):
#     box_quantity = math.ceil(number_items / items_per_box)
    
#     print(f"To place {number_items} items, packing {items_per_box} items in each box, you will need {box_quantity} boxes.")
    
# # Calling the function

# itemsinbox(number_items, items_per_box)


# import math

# def calcular_cajas(items, items_por_caja):
#   """Calcula el número de cajas necesarias."""
#   return math.ceil(items / items_por_caja)

# # Obtener datos del usuario
# items = int(input("Ingrese el número de items: "))
# items_por_caja = int(input("Ingrese el número de items por caja: "))

# # Calcular y mostrar el resultado
# resultado = calcular_cajas(items, items_por_caja)
# print(f"Se necesitan {resultado} cajas.")

print(Fore.RED + 'Este texto es rojo')
print(" ")
print(Back.GREEN + 'Este fondo es verde')
print(" ")
print(Style.BRIGHT + 'Texto brillante')