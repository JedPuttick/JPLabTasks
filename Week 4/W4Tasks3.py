def display_ladder(steps):
    # print("|  |")
    for i in range(steps):
        print("***")
        print("|  |")


def create_ladder():
    size = int(input("How many steps?"))
    display_ladder(size)


# create_ladder()

# -----

def sum_weights(character, inventory):
    TotalWeight = character + inventory
    return TotalWeight

def calc_avg_weight(character, inventory):
    AverageWeight = sum_weights(character, inventory) /2
    return AverageWeight

def run():
    CharWeight = int(input("Character weight: "))
    InvWeight = int(input("Inventory weight: "))
    SOA = input("Sum or average? ")
    if SOA.upper() == "SUM":
        print(sum_weights(CharWeight, InvWeight))
    elif SOA.upper() == "AVERAGE":
        print(calc_avg_weight(CharWeight, InvWeight))

run()