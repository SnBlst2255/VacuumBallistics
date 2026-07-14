import math
import plotext as plt

print("[!] This program uses simplified model of a thrown object. This program does NOT calculate the air resistance.\n[i] Press Enter to continue.")
input()

speed = 0
angle = 0
gravity = 0
points = 0
mass = 0

while speed <= 0:
    print("1) Enter speed (m/s):")
    speed = float(input())
    if speed > 0:
        break
    else:
        print("[X] Speed must be greater than zero.")

while mass <= 0:
    print("2) Enter mass (kg):")
    mass = float(input())
    if mass > 0:
        break;
    else:
        print("[X] Mass must be greater than zero.")

while angle <= 0 or angle >= 90:
    print("3) Enter throw angle (degrees):")
    angle = float(input())
    if 0 < angle < 90:
        break
    else:
        print("[X] Angle must be greater than zero and less than 90.")

while gravity <= 0:
    print("4) Enter the value of the acceleration due to gravity (m/s^2):")
    gravity = float(input())
    if gravity > 0:
        break
    else:
        print("[X] Acceleration must be greater than zero.")

while points <= 1:
    print("5) Enter the number of points for the trajectory table. The program will calculate the object's position (x, y) at each point of the flight. A larger number of points increases accuracy.")
    points = int(input())
    if points > 1:
        break
    else:
        print("[X] The number of points must be greater than 1.")


print("\n[i] Calculating...\n")

v0x = speed * math.cos(math.radians(angle))
v0y = speed * math.sin(math.radians(angle))
time = (2 * v0y) / gravity
flightRange = ((math.pow(speed, 2) * math.sin(math.radians(2*angle))))/gravity
height = math.pow(v0y, 2) / (2 * gravity)
momentum = mass * speed
energy_k = (mass * math.pow(speed, 2))/2
force = mass * gravity


print("Input data:")
print("Speed:", speed, "m/s")
print("Angle:", angle, "degrees")
print("Gravity acceleration(g):", gravity, "m/s^2")
print("Points:", points, "\n")

print("Velocity projection onto the x-axis:", round(v0x, 1), "m/s")
print("Velocity projection onto the y-axis:", round(v0y, 1), "m/s")
print("Flight time:", round(time, 1), "sec")
print("Flight range:", round(flightRange, 1), "m")
print("Maximum height:", round(height, 1), "m")
print("Initial momentum:", momentum, "kg*m/s")
print("Initial kinetic energy:", energy_k, "J")
print("Gravity force:", round(force, 1), "N\n")

interval = time / (points - 1)
timePoint = 0

x_points = []
y_points = []

x_points.append(0)
y_points.append(0)

spd = math.sqrt(math.pow(v0x,2) + math.pow(v0y, 2))

print(f"{'Point':<8}{'Time(sec)':<12}{'X-axis(m)':<12}{'Y-axis(m)':<12}{'E_k (J)':<12}{'E_p (J)':<12}{'p (kg * m/s)':<16}{'V (m/s)':<12}")
print(f"{1:<8}{'0':<12}{'0':<12}{'0':<12}{energy_k:<12}{'0':<12}{momentum:<16}{spd:<12}")
for i in range(2, points + 1):
    timePoint += interval

    x = abs(v0x * timePoint)
    y = abs(v0y * timePoint - ((gravity * math.pow(timePoint, 2)) / 2))
    x_points.append(x)
    y_points.append(y)

    V_y = v0y - gravity * timePoint
    spd = math.sqrt(math.pow(v0x,2) + math.pow(V_y, 2))

    E_k = (mass * math.pow(spd, 2))/2
    E_p = mass * gravity * y
    p = mass * spd

    print(f"{i:<8}{timePoint:<12.1f}{x:<12.1f}{y:<12.1f}{E_k:<12.1f}{E_p:<12.1f}{p:<16.1f}{spd:<12.1f}")

print("\n")
plt.scatter(x_points, y_points, color="white")
plt.title("Object Trajectory")
plt.xlabel("X, m")
plt.ylabel("Y, m")
plt.canvas_color("black")
plt.axes_color("black")
plt.ticks_color("white")
plt.show()

print("\n[!] Values are rounded. Small calculation errors can occur.")
print("[i] The program has finished executing. Press Enter to exit.")
input()
