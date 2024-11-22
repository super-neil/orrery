import pygame
import math
import numpy as np

speed = 0.025

class Planet:
    def __init__(self, distance_from_sun, orbital_speed, radius, color, x_position, y_position, time=0):
        self.distance_from_sun = distance_from_sun
        self.orbital_speed = orbital_speed
        self.radius = radius
        self.color = color
        self.angle = 0  # Position in its orbit
        self.x_position = x_position
        self.y_position = y_position
        self.time = 0

    def update_position(self):
        # Update the planet's position in its orbit
        # for every frame (i.e. per method call), calculate new position based on speed and distance from sun
        self.time += speed

        # Calculate the angle in radians
        self.angle = (self.orbital_speed * self.time) / self.distance_from_sun
        x = self.distance_from_sun * math.cos(self.angle)
        y = self.distance_from_sun * math.sin(self.angle)
        #print(f"""x: {x + 500}""")
        #print(f"""y: {y + 500}""")
        self.x_position = x + 500
        self.y_position = y + 500 


# Create planet instances...
sun = Planet(distance_from_sun=0, orbital_speed=0, radius=10, color=(255, 255, 0), x_position=500, y_position=500)

planet_array = []

mercury = Planet(distance_from_sun=9, orbital_speed=47.87, radius=5, color=(100, 100, 100), x_position=500, y_position=550)
venus = Planet(distance_from_sun=17, orbital_speed=35.02, radius=5, color=(255, 105, 180), x_position=500, y_position=600)
earth = Planet(distance_from_sun=24, orbital_speed=29.78, radius=5, color=(0, 0, 255), x_position=500, y_position=523)
mars = Planet(distance_from_sun=36, orbital_speed=24.07, radius=5, color=(255, 0, 0), x_position=500, y_position=700)
jupiter = Planet(distance_from_sun=124, orbital_speed=13.07, radius=5, color=(255, 255, 100), x_position=500, y_position=750)
saturn = Planet(distance_from_sun=229, orbital_speed=9.69, radius=5, color=(155, 155, 25), x_position=500, y_position=800)
uranus = Planet(distance_from_sun=461, orbital_speed=6.81, radius=5, color=(0, 50, 150), x_position=500, y_position=850)
neptune = Planet(distance_from_sun=721, orbital_speed=5.43, radius=5, color=(0, 100, 255), x_position=500, y_position=900)
pluto = Planet(distance_from_sun=950, orbital_speed=4.74, radius=5, color=(215, 215, 215), x_position=500, y_position=950)

planet_array.append(mercury)
planet_array.append(venus)
planet_array.append(earth)
planet_array.append(mars)
planet_array.append(jupiter)
planet_array.append(saturn)
planet_array.append(uranus)
planet_array.append(neptune)
planet_array.append(pluto)

# Initialize Pygame and create window...
pygame.init()
screen = pygame.display.set_mode((1000, 1000))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update planet positions
    for planet in planet_array:
      planet.update_position()

    # Draw everything
    screen.fill((0, 0, 0))  # Clear screen
    pygame.draw.circle(screen, sun.color, (sun.x_position, sun.y_position), sun.radius)

    for planet in planet_array:
      pygame.draw.circle(screen, planet.color, (planet.x_position, planet.y_position), planet.radius)

    pygame.display.flip()  # Update the display

pygame.quit()
