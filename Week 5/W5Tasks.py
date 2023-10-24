def directions():
    steps = ["Move Forward", "Move Backward", "Turn Left", "turn Right"]
    return steps


def run_task1():
    print(directions())


#run_task1()


# -------------

def movements():
    path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
    return path


def run_task2():
    print("Moving...")
    ThePath = movements()
    for i in range(0, len(ThePath) - 1, 2):
        print(f"{ThePath[i]} for {ThePath[i + 1]} steps")


#run_task2()

# ---------

def menu():
    print("Please select a direction: ")
    MyDirections = directions()
    for i in range(0, len(MyDirections)):
        print(f"{i} {MyDirections[i]}")

def run_task3():
    menu()

#run_task3()

# ---------

def menu_and_input():
    print("Please select a direction")
    MyDirections2 = directions()
    for i in range(0, len(MyDirections2)):
        print(f"{i}: {MyDirections2[i]}")
    selection = int(input("Selection: "))
    return MyDirections2[selection]

def run_task4():
    route = []
    print("Working out escape route...")
    for i in range(5):
        route.append(menu_and_input())
    print(f"Escape route: {route}")

#run_task4()