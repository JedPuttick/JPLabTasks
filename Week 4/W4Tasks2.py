def listen():
    sound = input("Make a sound: ")
    print(f"That was loud! {sound}!")


# listen()


# -------
def identify():
    sight = input("What do you see? ")
    if sight.upper() == "LARGE BOULDER":
        print("It's time to run!")
    else:
        print("We should be fine")


# identify()


# ------
def escape_by(plan):
    if plan.upper() == "JUMPING OVER":
        print("We can't the boulder is too big")
    elif plan.upper() == "RUNNING AROUND":
        print("We can't the boulder is too fast")
    elif plan.upper() == "CROSS BRIDGE AHEAD":
        print("That might work. Let's go!")
    else:
        print("That can't work!")


escape_by("Jumping over")
escape_by("running around")
escape_by("CROss briDge AHead")


# -------

def cross_bridge(steps):
    for i in range(steps):
        print("crossed step")
        if 5 > steps == i + 2:
            print("We must keep going!")
        elif i + 1 > 5:
            print("The bridge is collapsing")
        elif i + 1 == 7:
            print("The bridge has collapsed")


# distance = int(input("How many steps are there across the bridge? "))
# cross_bridge(distance)

# -------

def climb_ladder(remaining, crossed):
    if remaining > crossed:
        print("Long way to go!")
    else:
        print("Almost there!")


climb_ladder(5, 2)
climb_ladder(2, 5)
