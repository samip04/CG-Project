# Full 3D Solar System - All 8 Planets - VPython

from vpython import sphere, vector, color, rate, canvas
from math import cos, sin

# Set up fullscreen canvas
scene = canvas(fullscreen=True, background=color.black, title="Solar System Simulation")

# Create the Sun
sun = sphere(
    pos=vector(0, 0, 0),
    radius=2,
    color=color.yellow,
    emissive=True
)

# Planet data: (name, distance from sun, radius, color, speed)
planets_data = [
    ("Mercury", 3.5, 0.2, color.gray(0.5), 0.045),
    ("Venus", 5, 0.4, color.orange, 0.035),
    ("Earth", 7, 0.5, color.blue, 0.03),
    ("Mars", 9, 0.3, color.red, 0.024),
    ("Jupiter", 12, 0.9, color.orange, 0.013),
    ("Saturn", 15, 0.7, color.yellow, 0.01),
    ("Uranus", 18, 0.6, color.cyan, 0.007),
    ("Neptune", 21, 0.6, color.blue, 0.005)
]

# Create planet objects
planets = []
for name, distance, radius, col, speed in planets_data:
    planet = sphere(
        pos=vector(distance, 0, 0),
        radius=radius,
        color=col,
        make_trail=True,
        retain=150
    )
    planet.orbit_radius = distance
    planet.angle = 0
    planet.speed = speed
    planets.append(planet)

# Animate the Solar System
while True:
    rate(100)
    for planet in planets:
        planet.angle += planet.speed
        planet.pos = vector(
            planet.orbit_radius * cos(planet.angle),
            0,
            planet.orbit_radius * sin(planet.angle)
        )
