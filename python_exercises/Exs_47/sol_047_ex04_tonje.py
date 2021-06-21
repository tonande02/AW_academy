# a, b & c

import math

def kmh_to_ms(velocity):
    velocity_ms = velocity / 3.6
    return velocity_ms

def velocity_decomposition

def throw_distance(velocity, angle, init_height = 1.8):
    velocity_ms = kmh_to_ms(velocity)
    rad_angle = math.radians(angle)
    horizontal_velocity = velocity_ms * math.cos(rad_angle)
    vertical_velocity = velocity_ms * math.sin(rad_angle)
    air_time = (vertical_velocity + (math.sqrt( (vertical_velocity * vertical_velocity) + (2 * 9.81 * height)))) / 9.81
    throw_distance = horizontal_velocity * air_time
    
    return throw_distance


ang = int(input("Input angle: "))
vel = int(input("Input velocity (km/h): "))
height = int(input("Input height (m): "))

print(throw_distance(vel, ang))