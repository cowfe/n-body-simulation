from data import Planet, Config
import pygame
import simulator

image_sun = pygame.image.load('images/sun.png')
image_jupiter = pygame.image.load('images/jupiter.png')
image_earth = pygame.image.load('images/earth.png')
image_venus = pygame.image.load('images/venus.png')
image_uranus = pygame.image.load('images/uranus.png')
image_saturn = pygame.image.load('images/saturn.png')
image_mars = pygame.image.load('images/mars.png')
image_universe = pygame.image.load('images/universe.jpg')

def single():
    planets = [
        Planet(type='SUN', mass=2.0, position=[0.0, 0.0, 0.0], velocity=[0.1, 0.1, 0.0], image=image_sun, radius=20, trace_color=(206, 66, 87)),
        Planet(type='EARTH', mass=0.1, position=[0.0, 8.0, 0.0], velocity=[-0.5, 0.0, 0.0], image=image_earth, radius=5, trace_color=(0, 100, 150)),
    ]

    config = Config(
                dt=1, 
                trace_line_length=100, 
                screen_size=(1000, 800), 
                background_image=image_universe,
                rotation=[0, 0, 0],
                scale=8)

    return planets, config

def dual():
    planets = [
        Planet(type='SUN', mass=2.0, position=[0.0, 0.0, 0.0], velocity=[0.1, 0.1, 0.0], image=image_sun, radius=15, trace_color=(206, 66, 87)),
        Planet(type='SUN', mass=1.0, position=[0.0, 8.0, 0.0], velocity=[-0.5, 0.0, 0.0], image=image_sun, radius=10, trace_color=(63, 151, 155)),
        Planet(type='EARTH', mass=0.01, position=[-5.0, 25.0, 0.0], velocity=[-0.5, 0.0, 0.0], image=image_earth, radius=5, trace_color=(0, 100, 150)),
    ]

    config = Config(
                dt=0.5, 
                trace_line_length=40, 
                screen_size=(1000, 800), 
                background_image=image_universe,
                rotation=[0, 0, 0],
                scale=6)

    return planets, config

def three_1():
    planets = [
        Planet(type='SUN', mass=2.0, position=[0.0, 0.0, 0.0], velocity=[0.1, 0.1, 0.0], image=image_sun, radius=15, trace_color=(206, 66, 87)),
        Planet(type='SUN', mass=1.0, position=[0.0, 8.0, 0.0], velocity=[-0.5, 0.0, 0.0], image=image_sun, radius=10, trace_color=(63, 151, 155)),
        Planet(type='SUN', mass=1.0, position=[0.0, -18.0, 0.0], velocity=[-0.5, 0.0, 0.0], image=image_sun, radius=10, trace_color=(249, 74, 41)),
        Planet(type='EARTH', mass=0.01, position=[-5.0, 25.0, 0.0], velocity=[-0.4, 0.0, 0.0], image=image_earth, radius=5, trace_color=(0, 100, 150)),
    ]

    config = Config(
                dt=0.5, 
                trace_line_length=50, 
                screen_size=(1000, 800), 
                background_image=image_universe,
                rotation=[0, 0, 0],
                scale=10)

    return planets, config

# stable 3 body
def three_2():
    planets = [
        Planet(type='SUN', mass=1.2, position=[0.0, 0.0, 0.0], velocity=[0, 0.0, 0.0], image=image_sun, radius=12, trace_color=(206, 66, 87)),
        Planet(type='SUN', mass=1.0, position=[0.0, 13.0, 0.0], velocity=[-0.2, 0.0, 0.0], image=image_sun, radius=10, trace_color=(63, 151, 155)),
        Planet(type='SUN', mass=1.0, position=[0.0, -13.0, 0.0], velocity=[0.2, 0.0, 0.0], image=image_sun, radius=10, trace_color=(201, 180, 32)),
        #Planet(type='EARTH', mass=0.00001, position=[-1.1, 25.0, 0.0], velocity=[-0.151, 0.0, 0.0], image=image_earth, radius=5, trace_color=(0, 100, 150)),
    ]

    config = Config(
                dt=0.7, 
                trace_line_length=50, 
                screen_size=(1000, 800), 
                background_image=image_universe,
                rotation=[0, 0, 0],
                scale=10)

    return planets, config

def three_3():
    planets = [
        Planet(type='SUN', mass=1.2, position=[0.0, 0.0, 0.0], velocity=[0, 0.0, 0.0], image=image_sun, radius=12, trace_color=(206, 66, 87)),
        Planet(type='EARTH', mass=0.00001, position=[0.0, 5.0, 0.0], velocity=[-0.5, 0.0, 0.0], image=image_earth, radius=5, trace_color=(0, 100, 150)),
        Planet(type='SUN', mass=1.0, position=[0.0, 13.0, 0.0], velocity=[-0.2, 0.0, 0.0], image=image_sun, radius=10, trace_color=(63, 151, 155)),
        Planet(type='SUN', mass=1.0, position=[0.0, 30.0, 0.0], velocity=[0.2, 0.0, 0.0], image=image_sun, radius=10, trace_color=(201, 180, 32)),
    ]

    config = Config(
                dt=0.7, 
                trace_line_length=50, 
                screen_size=(1000, 800), 
                background_image=image_universe,
                rotation=[0, 0, 0],
                scale=10)

    return planets, config

def three_4():
    planets = [
        Planet(type='SUN', mass=1.2, position=[0.0, 0.0, 0.0], velocity=[0, 0.0, 0.0], image=image_sun, radius=12, trace_color=(206, 66, 87)),
        Planet(type='EARTH', mass=0.00001, position=[0.0, 5.0, 0.0], velocity=[-0.5, 0.0, 0.0], image=image_earth, radius=5, trace_color=(0, 100, 150)),
        Planet(type='EARTH', mass=0.00001, position=[0.0, -10.0, 0.0], velocity=[-0.5, 0.0, 0.0], image=image_earth, radius=5, trace_color=(0, 100, 150)),
        Planet(type='SUN', mass=1.0, position=[0.0, 13.0, 0.0], velocity=[-0.2, 0.0, 0.0], image=image_sun, radius=10, trace_color=(63, 151, 155)),
        Planet(type='SUN', mass=1.0, position=[0.0, 30.0, 0.0], velocity=[0.2, 0.0, 0.0], image=image_sun, radius=10, trace_color=(201, 180, 32)),
    ]

    config = Config(
                dt=0.5, 
                trace_line_length=50, 
                screen_size=(1000, 800), 
                background_image=image_universe,
                rotation=[1.1, 0.2, 0],
                scale=10)

    return planets, config

def solar():
    planets = [
        Planet(type='EARTH', mass=0.000001, position=[0, 15, 0.0], velocity=[-0.5, 0, 0.0], image=image_jupiter, radius=2, trace_color=(0, 100, 150)),
        Planet(type='EARTH', mass=0.000001, position=[0, 30, 0.0], velocity=[-0.3, 0.0, 0.0], image=image_venus, radius=5, trace_color=(117, 117, 117)),
        Planet(type='EARTH', mass=0.000001, position=[0, 45, 0.0], velocity=[-0.2, 0.0, 0.0], image=image_earth, radius=5, trace_color=(10, 80, 190)),
        Planet(type='EARTH', mass=0.000001, position=[0, 60, 0.0], velocity=[-0.15, 0.0, 0.0], image=image_mars, radius=5, trace_color=(70, 100, 210)),
        Planet(type='EARTH', mass=0.000001, position=[5, 80, 0.0], velocity=[-0.2, 0.0, 0.0], image=image_jupiter, radius=8, trace_color=(60, 132, 171)),
        Planet(type='EARTH', mass=0.000001, position=[10, 95, 0.0], velocity=[-0.21, 0.0, 0.0], image=image_saturn, radius=12, trace_color=(50, 100, 210)),
        Planet(type='EARTH', mass=0.000001, position=[20, 100, 0.0], velocity=[-0.25, 0.0, 0.0], image=image_jupiter, radius=6, trace_color=(20, 120, 210)),
        Planet(type='EARTH', mass=0.000001, position=[-10, 105, 0.0], velocity=[-0.15, 0.0, 0.0], image=image_uranus, radius=6, trace_color=(96, 150, 180)),
        Planet(type='EARTH', mass=0.000001, position=[0, 110, 0.0], velocity=[-0.25, 0.0, 0.0], image=image_jupiter, radius=2, trace_color=(50, 130, 190)),
        Planet(type='SUN', mass=5.0, position=[0, 0.0, 0.0], velocity=[0.0, 0.0, 0.0], image=image_sun, radius=20, trace_color=(206, 66, 87)),
    ]

    # check Config class definition
    config = Config(
                dt=2.5, 
                trace_line_length=500, 
                screen_size=(1000, 800), 
                background_image=image_universe,
                rotation=[1.0, 0.2, 0.0],
                scale=2.7)

    return planets, config

planets, config = solar()
#planets, config = single()
#planets, config = dual()
#planets, config = three_1()
#planets, config = three_2()
#planets, config = three_3()
#planets, config = three_4()

simulator.simulate(planets, config)
