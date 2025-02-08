#Water flow by Joaquin Leiva

#Global variables
EARTH_ACCELERATION_OF_GRAVITY = 9.8066500
WATER_DENSITY = 998.2000000
WATER_DYNAMIC_VISCOSITY = 0.0010016

PVC_SCHED80_INNER_DIAMETER = 0.28687  # meters
PVC_SCHED80_FRICTION_FACTOR = 0.013  # unitless
SUPPLY_VELOCITY = 1.65  # meters / second
HDPE_SDR11_INNER_DIAMETER = 0.048692  # meters
HDPE_SDR11_FRICTION_FACTOR = 0.018  # unitless
HOUSEHOLD_VELOCITY = 1.75  # meters / second


def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    """Calculates the pressure loss due to fittings."""
    return -0.04 * WATER_DENSITY * fluid_velocity**2 * quantity_fittings / 2000

def reynolds_number(hydraulic_diameter, fluid_velocity):
    """Calculates the Reynolds number."""
    return (WATER_DENSITY * hydraulic_diameter * fluid_velocity) / WATER_DYNAMIC_VISCOSITY

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    """Calculate the pressure loss due to pipe diameter reduction."""

    k = 0.1 + (50 / reynolds_number) * (((larger_diameter / smaller_diameter)**4) - 1)

    pressure_loss = - (k * WATER_DENSITY * fluid_velocity**2) / 2000

    return pressure_loss

def water_column_height(tower_height, tank_height):
    return tower_height + tank_height

def pressure_gain_from_water_height(water_height):
    return EARTH_ACCELERATION_OF_GRAVITY * WATER_DENSITY * water_height / 1000

def pressure_loss_from_pipe(diameter, length, friction_factor, fluid_velocity):
    g = EARTH_ACCELERATION_OF_GRAVITY
    hf = friction_factor * (length / diameter) * (fluid_velocity**2 / (2 * g))
    pressure_loss_pa = WATER_DENSITY * g * hf
    pressure_loss_kpa = pressure_loss_pa / 1000
    return -pressure_loss_kpa

def kPa_to_psi(kpa):
    """Converts pressure from kilopascals (kPa) to pounds per square inch (psi)."""
    return kpa * 0.145038

def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)

    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(diameter, velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY

    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss

if __name__ == "__main__":
    main()