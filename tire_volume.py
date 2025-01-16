# Import Modules
import math
from time import sleep
import platform
from datetime import datetime

def calculate_tire_volume(width, aspect, diam):  # Tire calculate function
    # Formula
    volume = math.pi * ((width / 1000) ** 2) * (aspect / 100) * ((width * (aspect / 100)) + (diam * 25.4))
    return round(volume, 2)
  
# Prices
def prices(width, aspect, diam):
    # Price based on width
    if width <= 199:
        width_price = 50
    elif 200 <= width <= 255:
        width_price = 70
    else:
        width_price = 90
    
    # Price based on aspect ratio
    if aspect <= 50:
        aspect_price = 30
    elif 51 <= aspect <= 99:
        aspect_price = 50
    else:
        aspect_price = 70
    
    # Price based on diameter
    if diam <= 15:
        diam_price = 40
    elif 16 <= diam <= 23:
        diam_price = 60
    else:
        diam_price = 80
    
    # Sum the prices for each category to calculate total price
    total_price = width_price + aspect_price + diam_price
    return total_price


def main():
    # Getting data from user
    print(" ")
    sleep(2)
    print("TIRE VOLUME CALCULATOR V 1.0")
    sleep(2)
    print(" ")
    name = input("Hello! What is your name? ")
    sleep(1)
    print(" ")
    print(f"Welcome to the Tire Volume Calculator, {name}!")
    sleep(1.5)
    print(" ")
    print("Please grab your tire information and enter the requested information.")
    sleep(1.5)
    print(" ")
    print("REMEMBER")
    sleep(2)
    print(" ")
    print("An example of Tire information is: 205/60R15. Forget about the / and R characters for now, focus on the numbers and their order :D")
    sleep(2)
    print(" ")
    print("In this case, the first number is 205, the second number is 60, and the third number is 15.")
    sleep(2)
    print(" ")
    print("Now let's find your tire volume!")
    sleep(1)
    print(" ")
    print("Ready?")
    print(" ")
    sleep(2)

    for i in range(3, 0, -1):
        print(i, flush=True)
        sleep(1)

    print(" ")
    width = float(input("Please enter the width of the tire in mm: "))
    sleep(0.8)
    print(" ")
    aspect = float(input("Please enter the aspect ratio: "))
    sleep(0.8)
    print(" ")
    diam = float(input("Please enter the diameter: "))
    sleep(0.8)
    print(" ")
    print(f"Thanks {name}, give us a second to calculate your tire volume.")
    sleep(1.5)
    print(" ")
    print("DONE")
    sleep(1)
    print(" ")
    
    # Calculate and display the result
    volume = calculate_tire_volume(width, aspect, diam)
    print(f"The approximate volume of your tire {name}, is {volume} liters.")
    sleep(1)

    print(" ")

    # Calculate the price using the prices function
    total_price = prices(width, aspect, diam)

    # Asking the user to buy the tires
    sleep(1)
    print(f"Congratulations {name}, we have a very special offer for these tires!")
    sleep(0.8)
    print(" ")
    print(f"The total price for your tire set is ${total_price}. Would you like to buy them?")
    sleep(0.5)
    print(" ")
    print("1. Yes")
    sleep(0.5)
    print(" ")
    print("2. No")
    print(" ")
    decision = input(f"Please enter your choice {name}: ")
    
    # Validate input for correct number choice
    while decision not in ['1', '2']:
        print(" ")
        print(f"Sorry that input is not valid. Please try again {name}")
        print(" ")
        print("Enter 1 for Yes or 2 for No.")
        print(" ")
        decision = input(f"Please enter your choice {name}: ")
        print(" ")

    if decision == "1":
        print(" ")
        sleep(1)
        phone = input(f"Great choice {name}!. Please enter your phone number, we'll contact you in the next 5 minutes: ")
        print(" ")
        # Get current date and system name and version
        current_date = datetime.now().strftime("%Y-%m-%d")
        os_system = platform.system()
        os_version = platform.version()
        
        # Write the info in the file
        # Write the info in the file
        with open("volumes.txt", "a") as file:
          file.write(f"{current_date} || width: {width} || aspect: {aspect} || diameter: {diam} || volume: {volume} || OS: {os_system} || Version: {os_version} || name: {name} || phone: {phone} || price: {total_price}\n")

    else:
        print(" ")
        print(f"No worries {name}! Your tire information won't be saved.")
        sleep(1)
        print (" ")

    # Thanks message
    print(f"Thanks for using our plattform {name}! Goodbye!")
    print(" ")
    sleep(0.8)
    print("##### CLOSING PROGRAM #####")
    print(" ")

# Function Main Calling
main()
