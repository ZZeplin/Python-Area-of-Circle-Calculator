GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"

pi = 3.14159

def areaOfCircle(r):
    return pi * r**2

def radiusFromDiameter(d):
    return d / 2

def circumferenceFromRadius(r):
    return 2 * pi * r

def circumferenceFromDiameter(d):
    return pi * d

def circumferenceFromArea(a):
    return 2*((pi*a)**0.5)

while True:
    print("What do you want to find?")
    print("-------------------------")
    print("For area, enter: 1")
    print("For circumference, enter: 2")
    print("To quit, enter: END")
    print("--------------------------\n")

    calculativeChoice = input("Enter your choice: ").strip().upper()

    if calculativeChoice == "END":
        print("Quitting...")
        break

    #choice to find the area
    if calculativeChoice == "1":
        print("From diameter or radius?")
        print("------------------------")
        print("For radius, enter: 1")
        print("For diameter, enter: 2")
        print("Return to selection, enter: RETURN")
        print("------------------------\n")

        userAreaChoice = input("Enter your choice: ").strip().upper()
        print()

        if userAreaChoice == "RETURN":
            continue

        if userAreaChoice not in ["1", "2", "RETURN"]:
            print(f"{RED}Invalid Input{RESET}\n")
            continue

        #Gets the area from the radius
        if userAreaChoice == "1":
            userRadius = input("Enter radius: ")
            print()
            try:
                circleRadius = float(userRadius)

                if circleRadius < 0:
                    print(f"{RED}Invalid Input: radius must be a non-negative value{RESET}\n")
                    continue

                print(f"{GREEN}Area = {areaOfCircle(circleRadius)}{RESET}\n")
            except ValueError:
                print(f"{RED}Invalid Input{RESET}\n")

        #Gets the area from the diameter and returns both radius and area
        if userAreaChoice == "2":
            userDiameter = input("Enter diameter: ")
            print()
            try:
                circleDiameter = float(userDiameter)

                if circleDiameter <= 0:
                    print(f"{RED}Invalid Input: const diameter > 0{RESET}\n")
                    continue

                circleRadius = radiusFromDiameter(circleDiameter)

                print(f"{GREEN}Radius = {circleRadius}{RESET}")
                print(f"{GREEN}Area = {areaOfCircle(circleRadius)}{RESET}\n")
            except ValueError:
                print(f"{RED}Invalid Input{RESET}\n")

    #Choice for finding the circumference
    if calculativeChoice == "2":
        print("From area, diameter, or radius?")
        print("-------------------------------")
        print("For diameter, enter: 1")
        print("For radius, enter: 2")
        print("For area, enter: 3")
        print("Return to selection, enter: RETURN")
        print("-------------------------------\n")

        userCircumChoice = input("Enter your choice: ").strip().upper()
        print()

        if userCircumChoice == "RETURN":
            continue

        if userCircumChoice not in ["1", "2", "3", "RETURN"]:
            print(f"{RED}Invalid Input{RESET}\n")
            continue

        #Gets the circumference from the diameter
        if userCircumChoice == "1":
            userDiameter = input("Enter diameter: ")
            print()
            try:
                circleDiameter = float(userDiameter)

                if circleDiameter <= 0:
                    print(f"{RED}Invalid Input: const diameter > 0{RESET}\n")
                    continue

                circleCircum = circumferenceFromDiameter(circleDiameter)
                print(f"{GREEN}Circumference = {circleCircum}{RESET}\n")
            except ValueError:
                print(f"{RED}Invalid Input{RESET}\n")

        #Gets the circumference from the radius
        if userCircumChoice == "2":
            userRadius = input("Enter radius: ")
            print()
            try:
                circleRadius = float(userRadius)

                if circleRadius < 0:
                    print(f"{RED}Invalid Input: radius must be a non-negative value{RESET}\n")
                    continue

                circleCircum = circumferenceFromRadius(circleRadius)
                print(f"{GREEN}Circumference = {circleCircum}{RESET}\n")
            except ValueError:
                print(f"{RED}Invalid Input{RESET}\n")

        #Gets the circumference from the area
        if userCircumChoice == "3":
            userArea = input("Enter area: ")
            print()
            try:
                circleArea = float(userArea)

                if circleArea <= 0:
                    print(f"{RED}Invalid Input: const area > 0{RESET}\n")
                    continue

                circleCircum = circumferenceFromArea(circleArea)
                print(f"{GREEN}Circumference = {circleCircum}{RESET}\n")
            except ValueError:
                print(f"{RED}Invalid Input{RESET}\n")
