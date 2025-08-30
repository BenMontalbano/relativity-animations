import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#Author: Ben Montalbano
#Purpose: This script will show the movement of particles as gravitational waves pass by. 
#This can be a very useful tool to demonstrate the polarizations of flat spacetime deviations that are 
#observed in the proper gauge of the weak field metric in the presence of gravitational waves.

# Constants (scaled for visualization)
c = 1e6  
L = 4000  
lambda_laser = 1064e-9  
f_gw = 0.4  
h0 = 1e-21  
omega = 2 * np.pi * f_gw  

# Time setup
duration = 5  
fps = 30 
t = np.linspace(0, duration, duration * fps)
h_t = h0 * np.sin(omega * t) 

# Phase shift calculation
delta_phi = (4 * np.pi * L / lambda_laser) * h_t

# Visual scaling
VISUAL_SCALE = 1e18 * 100  
scaled_h_t = h_t * VISUAL_SCALE
scaled_delta_phi = delta_phi * VISUAL_SCALE

# Setup figure and axes
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8))
plt.subplots_adjust(hspace=0.4)

# Interferometer Arms
mirror_x_line, = ax1.plot([], [], 'b-', linewidth=3, label='X arm')
mirror_y_line, = ax1.plot([], [], 'r-', linewidth=3, label='Y arm')
beam_splitter, = ax1.plot(0, 0, 'ko', markersize=6)

ax1.set_xlim(-500, 5000)
ax1.set_ylim(-500, 5000)
ax1.set_aspect('equal')
ax1.set_title("Interferometer Arm Deformation (L Shape, Exaggerated)")
ax1.set_xticks([])
ax1.set_yticks([])
ax1.legend()
ax1.grid(False)

# Phase Shift Plot
line_phase, = ax2.plot([], [], lw=2)
ax2.set_xlim(0, duration)
ax2.set_ylim(1.1 * scaled_delta_phi.min(), 1.1 * scaled_delta_phi.max())
ax2.set_title("Phase Shift Δφ(t) (scaled)")
ax2.set_xlabel("Time (s)")
ax2.set_ylabel("Phase Shift")
ax2.grid(True)

# Initialization function
def init():
    mirror_x_line.set_data([], [])
    mirror_y_line.set_data([], [])
    line_phase.set_data([], [])
    return mirror_x_line, mirror_y_line, line_phase

# Frame update function
def animate(i):
    h = scaled_h_t[i]

    # Apply strain to arm lengths
    delta_Lx = L * h / 2
    delta_Ly = L * h / 2

    # "L" shaped arms: start at origin, go positive
    mirror_x_line.set_data([0, L + delta_Lx], [0, 0])  
    mirror_y_line.set_data([0, 0], [0, L - delta_Ly])   

    line_phase.set_data(t[:i+1], scaled_delta_phi[:i+1])
    return mirror_x_line, mirror_y_line, line_phase

# Run the animation
ani = animation.FuncAnimation(
    fig, animate, frames=len(t),
    init_func=init, blit=True, interval=1000/fps
)

plt.show()
