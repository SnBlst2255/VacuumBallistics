import math

print("[!] This program uses simplified model of a thrown object. This program does NOT calculate the air resistance.\n[i] Press Enter to continue.")
input()

speed = 0
angle = 0
gravity = 0
points = 0

while speed <= 0:
    print("1) Enter speed (m/s):")
    speed = float(input())
    if speed > 0:
        break
    else:
        print("[X] Speed must be greater than zero.")

while angle <= 0 or angle >= 90:
    print("2) Enter throw angle (degrees):")
    angle = float(input())
    if 0 < angle < 90:
        break
    else:
        print("[X] Angle must be greater than zero and less than 90.")

while gravity <= 0:
    print("3) Enter the value of the acceleration due to gravity (m/s^2):")
    gravity = float(input())
    if gravity > 0:
        break
    else:
        print("[X] Acceleration must be greater than zero.")

while points <= 1:
    print("4) Enter the number of points for the trajectory table. The program will calculate the object's position (x, y) at each point of the flight. A larger number of points increases accuracy.")
    points = int(input())
    if points > 1:
        break
    else:
        print("[X] The number of points must be greater than 1.")

print("\n[i] Calculating...\n")

V0x = speed * math.cos(math.radians(angle))
V0y = speed * math.sin(math.radians(angle))
time = (2 * V0y) / gravity
flightRange = ((math.pow(speed, 2) * math.sin(math.radians(2*angle))))/gravity
height = math.pow(V0y, 2) / (2 * gravity)

print("Input data:")
print("Speed:", speed, "m/s")
print("Angle:", angle, "degrees")
print("Gravity acceleration(g):", gravity, "m/s^2")
print("Points:", points, "\n")

print("Velocity projection onto the x-axis:", V0x, "m/s")
print("Velocity projection onto the y-axis:", V0y, "m/s")
print("Flight time:", round(time, 2), "sec")
print("Flight range:", round(flightRange,2), "m")
print("Maximum height:", round(height, 2), "m")

interval = time / (points - 1)
timePoint = 0
print(f"{'Point':<8}{'Time(sec)':<12}{'X-axis(m)':<12}{'Y-axis(m)':<12}")
print(f"{1:<8}{'0':<12}{'0':<12}{'0':<12}")
for i in range(2, points + 1):
    timePoint += interval
    x = V0x * timePoint
    y = V0y * timePoint - ((gravity * math.pow(timePoint, 2)) / 2)
    print(f"{i:<8}{timePoint:<12.2f}{x:<12.2f}{y:<12.2f}")

print("\n[!] Values are rounded. Small calculation errors can occur.")
print("[i] The program has finished executing. Press Enter to exit.")
input()