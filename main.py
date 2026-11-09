def areaOfCircle(radius):
    r = radius**2
    pi = 3.14159
    area = pi * r
    return area

while True:
    raw = input("Enter radius (enter END to quit): ")

    if raw.strip().upper() == "END":
        print("Ending")
        break

    try:
        circleRadius = float(raw)

        if circleRadius < 0:
            print("Invalid Input: radius mustn't be negative")
            continue

        print(areaOfCircle(circleRadius))
    except ValueError:
        print("Invalid Input")