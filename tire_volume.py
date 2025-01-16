#Importing modules
import math
from time import sleep


def calculate_tire_volume(width, aspect, diam): #Tire calculate function
    
    # Formula
    volume = math.pi * ((width / 1000)**2) * (aspect / 100) * ((width * (aspect / 100)) + (diam * 25.4))
    return round(volume, 2)

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
    print("Please grab your tire information and enter the requested information")
    sleep(1.5)
    print(" ")
    print("REMEMBER")
    sleep(2)
    print(" ")
    print("An example of Tire information is: 205/60R15.")
    print(" ")
    sleep(2)
    print("Forget about the 7 and R character for now, focus on the numbers and their order :D")
    sleep(2)
    print(" ")
    print("In this case the first number is 205, the second number is 60 and the third number is 15.")
    sleep(2)
    print(" ")
    sleep(1.5)
    print("Now let's find your tire volume!")
    sleep(1)
    print(" ")
    print("Ready?")
    print(" ")
    sleep(2)
    
    for i in range(3, 0, -1):
        print(i, flush=True)
        sleep(1) 

    sleep(2)
    
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
    # Output
    print(f"The approximate volume of you tire {name}, is {calculate_tire_volume(width, aspect, diam)} liters.")
    sleep(1)
    print(" ")
    print("Thanks for using our plattform! GoodBye")
    print(" ")

# Function Main Calling
main()