from numpy import matrix
from math import cos, sin, pi

###########################
# 3D Math
###########################
def generate_x(theta):
    return matrix([
        [1, 0, 0],
        [0, cos(theta), -sin(theta)],
        [0, sin(theta), cos(theta)]
    ])

def generate_y(theta):
    return matrix([
        [cos(theta), 0, -sin(theta)],
        [0, 1, 0],
        [sin(theta), 0, cos(theta)]
    ])

def generate_z(theta):
    return matrix([
        [cos(theta), -sin(theta), 0],
        [sin(theta), cos(theta), 0],
        [0, 0, 1]
    ])

###########################
# 2D Math
###########################
# convert world coordinates to screen
# cx, cy - viewport x, y
def world_2_screen(point: tuple, cx: float, cy: float, rotation: list, zoom_in_factor: float):
    point = matrix((
        (point[0], point[1], point[2])
    )).transpose()

    # 3D transform
    for method, angle in zip((generate_x, generate_y, generate_z), rotation):
        point = method(angle) * point

    # project to screen    
    x, y = point[0], point[1]
    x = int((x - cx) * zoom_in_factor) + 500
    y = int((y - cy) * zoom_in_factor) + 300

    return x, y

# change color
def dim_color(color, f: float):
    return tuple(int(c * f) for c in color)