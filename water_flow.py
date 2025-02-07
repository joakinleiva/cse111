# water_flow.py

# Constants
DENSITY_WATER = 998.2  # kg/m^3
DYNAMIC_VISCOSITY_WATER = 0.0010016  # Pascal·seconds

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    """Calculates the pressure loss due to fittings."""
    return -0.04 * DENSITY_WATER * fluid_velocity**2 * quantity_fittings / 2000

def reynolds_number(hydraulic_diameter, fluid_velocity):
    """Calculates the Reynolds number."""
    return (DENSITY_WATER * hydraulic_diameter * fluid_velocity) / DYNAMIC_VISCOSITY_WATER

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    """Calculate the pressure loss due to pipe diameter reduction."""
    density_water = 998.2  # kg/m^3

    # Compute k (Make sure this formula is correct for your scenario)
    k = 0.1 + (50 / reynolds_number) * (((larger_diameter / smaller_diameter)**4) - 1)

    # Compute pressure loss
    pressure_loss = - (k * density_water * fluid_velocity**2) / 2000

    #print(f"k: {k}, Pressure Loss: {pressure_loss}")  # Debugging print statement (optional)

    return pressure_loss

PVC_SCHED80_INNER_DIAMETER = 0.28687  # meters
PVC_SCHED80_FRICTION_FACTOR = 0.013  # unitless
SUPPLY_VELOCITY = 1.65  # meters / second
HDPE_SDR11_INNER_DIAMETER = 0.048692  # meters
HDPE_SDR11_FRICTION_FACTOR = 0.018  # unitless
HOUSEHOLD_VELOCITY = 1.75  # meters / second

def water_column_height(tower_height, tank_height):
    return tower_height + tank_height

def pressure_gain_from_water_height(water_height):
    return 9.81 * DENSITY_WATER * water_height / 1000

def pressure_loss_from_pipe(diameter, length, friction_factor, fluid_velocity):
    g = 9.81  # m/s^2
    hf = friction_factor * (length / diameter) * (fluid_velocity**2 / (2 * g))
    pressure_loss_pa = DENSITY_WATER * g * hf
    pressure_loss_kpa = pressure_loss_pa / 1000  # Convert to kPa
    return -pressure_loss_kpa  # Pressure loss is negative

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
    print(f"Pressure at house: {pressure:.1f} kilopascals")

if __name__ == "__main__":
    main()