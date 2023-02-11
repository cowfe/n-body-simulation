from typing import List
from data import Planet, Config
import numpy as np
from collections import deque
import pygame
import physics, graphics

###########################
# Drawing
###########################
# draw a planet
def draw_planet(screen, planet: Planet, point: tuple, cx: float, cy: float, rotation: tuple, scale: float):
    length = int(planet.radius * 2)
    size = (length, length)
    resized_image = pygame.transform.scale(planet.image, size)
    x, y = graphics.world_2_screen(point, cx, cy, rotation, scale)
    radius = planet.radius
    screen.blit(resized_image, (x - radius, y - radius))
    return x, y

# draw a trace line
def draw_trace(screen, planet: Planet, trace: List):
    pos_list = list(trace)
    N = len(pos_list)
    for i in range(1, N):
        (x0, y0) = trace[i - 1]
        (x1, y1) = trace[i]
        color = graphics.dim_color(planet.trace_color, (i + 1) / N)
        pygame.draw.line(screen, color, (x0, y0), (x1, y1), width=2)

###########################
# Simulation
###########################        
def simulate(planets: List[Planet], config: Config):
    # data init
    N = len(planets)
    masses = np.array([d.mass for d in planets])
    positions = np.array([d.position for d in planets])
    velocities = np.array([d.velocity for d in planets])
    dt = config.dt

    # queue to store last X positions
    traces = []
    for i in range(N):
        traces.append(deque(maxlen=int(config.trace_line_length / dt)))

    # PyGame setup
    pygame.init()
    screen_size = config.screen_size
    screen = pygame.display.set_mode(screen_size)
    image_background = pygame.transform.scale(config.background_image, screen_size)
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # calculate the next position
        positions, velocities = physics.verlet(positions, velocities, masses, dt)

        # draw background
        screen.blit(image_background, (0, 0))

        # calculate the center of mass
        cx, cy = physics.center_of_mass(positions, masses)

        # draw planets
        for i in range(N):
            draw_trace(screen, planets[i], trace=traces[i])
            x, y = draw_planet(screen, planet=planets[i], point=positions[i], 
                               cx=cx, cy=cy, 
                               rotation=config.rotation,
                               scale=config.scale)
            
            # save last position for trace drawing
            traces[i].append((x, y))

        pygame.display.update()
        clock.tick(60)

    pygame.quit()