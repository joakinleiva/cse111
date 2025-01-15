import math
TO_MIL = float(25.4)

# Data from user

width_tire = int(input("Insert the 1st number: "))
aspect_ratio = int(input("Insert the 2nd number: "))
diameter_wheel = int(input("Insert the 3rd number: "))

height_sidewall = (aspect_ratio / 100) * width_tire # Height of the sidewall
radius = (TO_MIL * diameter_wheel) / 2 # Radius

# Cilynder formula
volume_cilynder = math.pi * radius ** 2 * height_sidewall

inner =
outer =
volume_tire = inner - outer










def tire_volume(w, a, d):
  return (math.pi * w**2 * a * (a + 2540 * d)) / 10000000000

w = 205
a = 60
d = 15

volume = tire_volume(w, a, d)
print(volume) 