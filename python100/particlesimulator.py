import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class CelestialBody:
    def __init__(self, name, mass, position, velocity, color):
        self.name = name
        self.mass = mass
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        self.color = color

class SolarSystem:
    G = 6.67430e-11  # Gravitational constant
    
    def __init__(self, bodies):
        self.bodies = bodies
        self.time = 0
        
    def gravitational_force(self, body1, body2):
        r = body2.position - body1.position
        distance = np.linalg.norm(r)
        force_magnitude = self.G * body1.mass * body2.mass / (distance ** 2)
        force = force_magnitude * r / distance
        return force
    
    def total_force(self, body):
        total_force = np.zeros(2)
        for other_body in self.bodies:
            if other_body != body:
                force = self.gravitational_force(body, other_body)
                total_force += force
        return total_force
    
    def update(self, dt):
        for body in self.bodies:
            force = self.total_force(body)
            acceleration = force / body.mass
            body.position += body.velocity * dt + 0.5 * acceleration * dt**2
            new_force = self.total_force(body)
            new_acceleration = new_force / body.mass
            body.velocity += 0.5 * (acceleration + new_acceleration) * dt
        self.time += dt

# Create celestial bodies
sun = CelestialBody("Sun", 1.989e30, [0, 0], [0, 0], 'yellow')
earth = CelestialBody("Earth", 5.97e24, [1.496e11, 0], [0, 29.78e3], 'blue')
mars = CelestialBody("Mars", 6.39e23, [2.279e11, 0], [0, 24.077e3], 'red')
venus = CelestialBody("Venus", 4.867e24, [1.082e11, 0], [0, 35.02e3], 'orange')

solar_system = SolarSystem([sun, earth, mars, venus])

# Set up the plot
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_xlim(-2.5e11, 2.5e11)
ax.set_ylim(-2.5e11, 2.5e11)
ax.set_aspect('equal')
ax.set_title("Solar System Simulation")

lines = [ax.plot([], [], 'o-', lw=2, color=body.color)[0] for body in solar_system.bodies]
trails = [ax.plot([], [], '-', lw=1, color=body.color, alpha=0.3)[0] for body in solar_system.bodies]

time_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)

def init():
    for line in lines:
        line.set_data([], [])
    for trail in trails:
        trail.set_data([], [])
    time_text.set_text('')
    return lines + trails + [time_text]

trail_data = [[] for _ in solar_system.bodies]

def update(frame):
    solar_system.update(86400)  # Update every day
    
    for i, (body, line, trail) in enumerate(zip(solar_system.bodies, lines, trails)):
        x, y = body.position
        line.set_data(x, y)
        
        trail_data[i].append((x, y))
        if len(trail_data[i]) > 365:  # Keep only last year's trail
            trail_data[i].pop(0)
        trail.set_data(*zip(*trail_data[i]))
    
    time_text.set_text(f'Time: {solar_system.time / 86400:.0f} days')
    return lines + trails + [time_text]

anim = FuncAnimation(fig, update, frames=365, init_func=init, blit=True, interval=20)
plt.show()