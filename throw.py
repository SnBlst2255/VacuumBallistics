import math
import plotext as plt

def getData():

    speed = 0
    angle = 0
    gravity = 0
    points = 0
    mass = 0

    while speed <= 0:
        print("1) Enter speed (m/s):")
        speed = float(input("> "))
        if speed > 0:
            break
        else:
            print("[X] Speed must be greater than zero.")

    while mass <= 0:
        print("2) Enter mass (kg):")
        mass = float(input("> "))
        if mass > 0:
            break;
        else:
            print("[X] Mass must be greater than zero.")

    while angle <= 0 or angle >= 90:
        print("3) Enter throw angle (degrees):")
        angle = float(input("> "))
        if 0 < angle < 90:
            break
        else:
            print("[X] Angle must be greater than zero and less than 90.")

    while gravity <= 0:
        print("4) Enter the value of the acceleration due to gravity (m/s^2):")
        gravity = float(input("> "))
        if gravity > 0:
            break
        else:
            print("[X] Acceleration must be greater than zero.")

    while points <= 1:
        print("5) Enter the number of points for the trajectory table.")
        points = int(input("> "))
        if points > 1:
            break
        else:
            print("[X] The number of points must be greater than 1.")
    
    data = {
        "speed": speed,
        "angle": angle,
        "gravity": gravity,
        "points": points,
        "mass": mass
    }

    return data

def displayMenu():
    print("\n==================== MAIN MENU ====================\n")
    print("All calculations have been completed.")
    print("Select the data you would like to display.\n")
    print("1) Show input data")
    print("2) Show calculated characteristics")
    print("3) Show trajectory table")
    print("4) Show trajectory graph")
    print("5) Enter new input data")
    print("0) Exit\n")

def main():
    print("[!] This program uses simplified model of a thrown object. This program does NOT calculate the air resistance.\n[i] Press Enter to continue.")
    input()
    data = getData()

    while True:
        displayMenu()
        option = int(input("Enter your choice: "))
        if option == 1:
            displayData(data) 
        elif option == 2:
            displayCharacteristics(data)
        elif option == 3:
            calcTable(data, True)
        elif option == 4:
            displayGraph(calcTable(data, False))
        elif option == 5:
            data = getData()
            displayMenu()
        elif option == 0:
            quit()

def displayData(data):
    print("\n==================== INPUT DATA ====================\n")
    print("Speed:", data["speed"], "m/s")
    print("Angle:", data["angle"], "degrees")
    print("Gravity acceleration(g):", data["gravity"], "m/s^2")
    print("Mass:", data["mass"], "kg")
    print("Points:", data["points"], "\n")

    print("Press enter to return to the Menu.")
    input()

def calcChar(data):
    v0x = data["speed"] * math.cos(math.radians(data["angle"]))
    v0y = data["speed"] * math.sin(math.radians(data["angle"]))
    time = (2 * v0y) / data["gravity"]
    flightRange = ((math.pow(data["speed"], 2) * math.sin(math.radians(2*data["angle"]))))/data["gravity"]
    height = math.pow(v0y, 2) / (2 * data["gravity"])
    momentum = data["mass"] * data["speed"]
    energy_k = (data["mass"] * math.pow(data["speed"], 2))/2
    force = data["mass"] * data["gravity"]

    charData = {
        "v0x": v0x,
        "v0y": v0y,
        "time": time,
        "flightRange": flightRange,
        "height": height,
        "momentum": momentum,
        "energy_k": energy_k,
        "force": force
    }

    return charData

def displayCharacteristics(data):
    chars = calcChar(data)

    print("\n==================== CHARACTERISTICS ====================\n")
    print("Velocity projection onto the x-axis:", round(chars["v0x"], 1), "m/s")
    print("Velocity projection onto the y-axis:", round(chars["v0y"], 1), "m/s")
    print("Flight time:", round(chars["time"], 1), "sec")
    print("Flight range:", round(chars["flightRange"], 1), "m")
    print("Maximum height:", round(chars["height"], 1), "m")
    print("Initial momentum:", chars["momentum"], "kg*m/s")
    print("Initial kinetic energy:", chars["energy_k"], "J")
    print("Gravity force:", round(chars["force"], 1), "N\n")

    print("Press enter to return to the Menu.")
    input()

def calcTable(data, display):
    chars = calcChar(data)

    interval = chars["time"] / (data["points"] - 1)
    timePoint = 0

    x_points = []
    y_points = []

    x_points.append(0)
    y_points.append(0)

    spd = math.sqrt(math.pow(chars["v0x"],2) + math.pow(chars["v0y"], 2))

    if display:
        print("\n==================== TABLE ====================\n")
        print(f"{'Point':<8}{'Time(sec)':<12}{'X-axis(m)':<12}{'Y-axis(m)':<12}{'E_k (J)':<12}{'E_p (J)':<12}{'p (kg * m/s)':<16}{'V (m/s)':<12}")
        print(f"{1:<8}{'0':<12}{'0':<12}{'0':<12}{chars["energy_k"]:<12}{'0':<12}{chars["momentum"]:<16}{round(spd, 1):<12}")
    
    for i in range(2, data["points"] + 1):
        timePoint += interval

        x = abs(chars["v0x"] * timePoint)
        y = abs(chars["v0y"] * timePoint - ((data["gravity"] * math.pow(timePoint, 2)) / 2))
        x_points.append(x)
        y_points.append(y)

        V_y = chars["v0y"] - data["gravity"] * timePoint
        spd = math.sqrt(math.pow(chars["v0x"],2) + math.pow(V_y, 2))

        E_k = (data["mass"] * math.pow(spd, 2))/2
        E_p = data["mass"] * data["gravity"] * y
        p = data["mass"] * spd

        if display:
            print(f"{i:<8}{timePoint:<12.1f}{x:<12.1f}{y:<12.1f}{E_k:<12.1f}{E_p:<12.1f}{p:<16.1f}{spd:<12.1f}")

    if display:
        print("Press enter to return to the Menu.")
        input()

    table = {
        "x_points": x_points,
        "y_points": y_points
    }

    return table

def displayGraph(table):
    print("\n==================== GRAPH ====================\n")
    plt.clear_figure()
    plt.scatter(table["x_points"], table["y_points"], color="white")
    plt.title("Object Trajectory")
    plt.xlabel("X, m")
    plt.ylabel("Y, m")
    plt.canvas_color("black")
    plt.axes_color("black")
    plt.ticks_color("white")
    plt.show()

    print("\nPress enter to return to the Menu.")
    input()

main()
