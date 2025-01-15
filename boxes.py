# #Boxes by Joaquin Leiva
import math

from colorama import *
init()

number_items = int(input("Insert the number of items: ")) # Asking for the number of items
print(" ") #Spacing
items_per_box = int(input("How many items you'd like to pack in each box?: ")) # Asking for the number of items per box

# #Function 

def itemsinbox(number_items, items_per_box):
    box_quantity = math.ceil(number_items / items_per_box)
    print(f"To place {number_items} items, packing {items_per_box} items in each box, you will need {box_quantity} boxes.")
    
# Calling the function

itemsinbox(number_items, items_per_box)
