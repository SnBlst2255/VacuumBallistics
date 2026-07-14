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
  - Kinetic energy
  - Potential energy
  - Momentum
  - Speed
- Generates a trajectory table:
  - Point number
  - Time
  - X position
  - Y position
  - Kinetic energy
  - Potential energy
  - Momentum
  - Speed
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

### Kinetic energy

$$
E_k=\frac{mv^2}{2}
$$

### Potential energy

$$
E_p=mgh
$$

### Momentum

$$
p=mv
$$

Where:

- $m$ — object mass (kg)
- $v$ — object speed (m/s)
- $h$ — height above the launch point (m)
- $g$ — acceleration due to gravity (m/s²)
- $E_k$ — kinetic energy (J)
- $E_p$ — potential energy (J)
- $p$ — momentum (kg·m/s)

> [!WARNING]
> Furthermore, the current physical model assumes that the acceleration due to gravity is constant and that the Earth's surface is locally flat. These assumptions are valid for projectile motion over relatively short distances and at low altitudes. For long-range trajectories or high altitudes, the acceleration due to gravity decreases with altitude, and the curvature of the Earth can no longer be neglected.

## Example Output

```text
[i] Calculating...

Input data:
Speed: 12.0 m/s
Angle: 35.0 degrees
Gravity acceleration(g): 9.8 m/s^2
Points: 10 

Velocity projection onto the x-axis: 9.83 m/s
Velocity projection onto the y-axis: 6.88 m/s
Flight time: 1.4 sec
Flight range: 13.81 m
Maximum height: 2.42 m
Initial momentum: 36.0 kg*m/s
Initial kinetic energy: 216.0 J
Gravity force: 29.4 N

Point   Time(sec)   X-axis(m)   Y-axis(m)   E_k (J)     E_p (J)     p (kg * m/s)    V (m/s)     
1       0           0           0           216.0       0           36.0            12.0        
2       0.2         1.5         1.0         187.9       28.1        33.6            11.2        
3       0.3         3.1         1.7         166.9       49.1        31.6            10.5        
4       0.5         4.6         2.1         152.8       63.2        30.3            10.1        
5       0.6         6.1         2.4         145.8       70.2        29.6            9.9         
6       0.8         7.7         2.4         145.8       70.2        29.6            9.9         
7       0.9         9.2         2.1         152.8       63.2        30.3            10.1        
8       1.1         10.7        1.7         166.9       49.1        31.6            10.5        
9       1.2         12.3        1.0         187.9       28.1        33.6            11.2        
10      1.4         13.8        0.0         216.0       0.0         36.0            12.0       

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