import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#Author: Ben Montalbano
#Purpose: This script will show the movement of particles as gravitational waves pass by. 
#This can be a very useful tool to demonstrate the polarizations of flat spacetime deviations that are 
#observed in the proper gauge of the weak field metric in the presence of gravitational waves.

# Define Constants
f = 1
omega = 2 * np.pi * f 
plus_Pol = 0.2
cross_Pol = 0.2

# Create a ring of particles
num_particles = 20
angles = np.linspace(0, 2 * np.pi, num_particles)
x = np.cos(angles)
y = np.sin(angles)

# Compute Gravitational Wave Displacement
def wave_shift(t):
    h_plus = plus_Pol * np.cos(omega * t)
    h_cross = cross_Pol * np.sin(omega * t)
    
    x_new = x + h_plus * x + h_cross * y
    y_new = y - h_plus * y + h_cross * x
    
    return x_new, y_new

# Set up the plot
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_title("Gravitational Wave Effect on Particles")

points, = ax.plot([], [], 'bo')

def Animate_start():
    points.set_data([], [])
    return points,

# Animation function
def Animate_shift(i):
    t = i / 20.0
    x_new, y_new = wave_shift(t)
    points.set_data(x_new, y_new)
    return points,

# Create animation
ani = animation.FuncAnimation(fig, Animate_shift, frames=200, init_func=Animate_start, interval=60)
plt.show()