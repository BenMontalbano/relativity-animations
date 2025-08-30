# relativity-animations
This repository contains scripts that produce animations of General Relativistic phenomena for educational purposes.

Two compact Python animations that demonstrate how gravitational waves deform space: (1) interferometer arm strain and phase shift, and (2) particle ring distortions showing **+** and **×** polarizations.

---

## Overview

This project contains two educational simulations for visualizing weak-field gravitational wave effects:

1. **Interferometer Phase Shift** — Shows how a passing GW stretches/shrinks the arms of an L-shaped interferometer and how this induces a time-varying phase shift Δφ(t) in the laser light.
2. **Polarization Ring** — Animates a ring of free test particles to illustrate the characteristic **plus** and **cross** polarization patterns.

Both scripts are self-contained, use standard scientific Python, and are optimized for clarity as teaching/demo tools.

---

## Features

- Interferometer arm strain \(h(t)\) and corresponding **phase shift Δφ(t)** plot
- Exaggeration/scaling for clear, classroom-friendly visuals
- Particle-ring animation exhibiting **+** and **×** GW polarizations
- Simple, readable code structure (NumPy math + Matplotlib animation)
- No external data required

---

## Technology Stack

- **Python**: NumPy, Matplotlib
- **Visualization**: Matplotlib (2D + animation)

---

## Installation

```bash
git clone https://github.com/BenMontalbano/gravitational-wave-visualizations.git
cd gravitational-wave-visualizations
pip install numpy matplotlib
