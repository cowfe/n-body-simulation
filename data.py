from dataclasses import dataclass

@dataclass
class Planet:
    type: str           # SUN or EARTH
    mass: float         # mass
    position: list      # position [x, y, z]
    velocity: list      # velocity [vx, vy, vz]
    image: object       # image instance
    radius: float       # radius
    trace_color: tuple  # color (R, G, B)

@dataclass
class Config:
    dt: float                   # time interval
    trace_line_length: int      # length of the trace
    screen_size: tuple          # size (width, height)
    background_image: object    # background image instance
    rotation: tuple             # [x, y, z] rotation
    zoom_in_factor: float       # screen zoom in control