import math

angle = int(input("Input angle: "))
velocity = int(input("Input velocity (km/h): "))
height = int(input("Input height (m): "))
print()

# i
rad_angle = math.radians(angle)
print(f"Calculated angle: {rad_angle:.2f}")

# ii
velocity_ms = velocity / 3.6
print(f"Calculated velocity: {velocity_ms:.2f}")

# iii
horizontal_velocity = velocity_ms * math.cos(rad_angle)
print(f"Horizontal velocity: {horizontal_velocity:.2f}")

# iv
vertical_velocity = velocity_ms * math.sin(rad_angle)
print(f"Vertical velocity: {vertical_velocity:.2f}")

# v
air_time = (vertical_velocity + (math.sqrt( (vertical_velocity * vertical_velocity) + (2 * 9.81 * height)))) / 9.81
print(f"Air time: {air_time:.2f}")

# vi
throw_distance = horizontal_velocity * air_time
print(f"Throw distance: {throw_distance:.2f}")


# d)
# ok

# e)
# ok

# f)
# meh :3