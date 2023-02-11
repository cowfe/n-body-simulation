import numpy as np

###########################
# Math in physics
###########################

def compute_acceleration(positions, masses):
    N = positions.shape[0]
    acceleration = np.zeros_like(positions)
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            delta = positions[j] - positions[i]
            distance = np.linalg.norm(delta)
            acceleration[i] += masses[j] * delta / distance**3

    return acceleration

def verlet(positions, velocities, masses, dt):
    N = positions.shape[0]
    acceleration = compute_acceleration(positions, masses)
    new_positions = positions + dt * velocities + 0.5 * dt**2 * acceleration
    new_acceleration = compute_acceleration(new_positions, masses)
    new_velocities = velocities + 0.5 * dt * (acceleration + new_acceleration)
    return new_positions, new_velocities

# calculate the center of mass
def center_of_mass(positions, masses):
    N = positions.shape[0]
    cx = 0.0
    cy = 0.0
    for i in range(N):
        x = positions[i][0] 
        y = positions[i][1] 
        cx += x * masses[i]
        cy += y * masses[i]

    cx = cx / masses.sum()
    cy = cy / masses.sum()

    return cx, cy