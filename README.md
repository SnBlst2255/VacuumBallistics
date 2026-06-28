# Vacuum Ballistics

A simple Python program for simulating projectile motion in a vacuum.

> [!WARNING]
> This program uses a simplified physical model and does **not** take air resistance into account.

## Features

- Calculates:
  - Initial velocity components
  - Flight time
  - Maximum height
  - Flight range
- Generates a trajectory table:
  - Time
  - X position
  - Y position
- Validates user input
- Supports any value of gravitational acceleration
- Shows graph

> [!NOTE]
> The main idea behind this model is that projectile motion can be split into two independent motions: horizontal motion and vertical motion.

The program calculates the flight time, maximum height, and flight range using the equations below.

To generate the trajectory table, the total flight time is divided into equal intervals. The object's position is then calculated at each point. The user chooses the number of points before the calculation starts.

## Equations

### Flight time

$$
T=\frac{2v_0\sin\alpha}{g}
$$

### Maximum height

$$
H=\frac{v_0^2\sin^2\alpha}{2g}
$$

### Flight range

$$
R=\frac{v_0^2\sin(2\alpha)}{g}
$$

Where:

- $v_0$ — initial velocity (m/s)
- $\alpha$ — launch angle
- $g$ — acceleration due to gravity (m/s²)
- $T$ — flight time
- $H$ — maximum height
- $R$ — flight range

## Example output

```text
[i] Calculating...

Input data:
Speed: 75.0 m/s
Angle: 60.0 degrees
Gravity acceleration (g): 9.81 m/s²
Points: 10

Velocity projection onto the x-axis: 37.5 m/s
Velocity projection onto the y-axis: 64.95 m/s
Flight time: 13.24 sec
Flight range: 496.57 m
Maximum height: 215.02 m

Point   Time(sec)   X-axis(m)   Y-axis(m)
1       0.00        0.00        0.00
2       1.47        55.17       84.95
3       2.94        110.35      148.66
4       4.41        165.52      191.13
5       5.89        220.70      212.37
6       7.36        275.87      212.37
7       8.83        331.05      191.13
8       10.30       386.22      148.66
9       11.77       441.40      84.95
10      13.24       496.57      0.00

*Graph*
```

## Installation

Install the required library:

```bash
pip install plotext
```

Then run the program:

```bash
python throw.py
```