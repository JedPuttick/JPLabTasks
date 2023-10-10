mountains = int(input("How many mountains should I display? "))

for i in range(mountains):
    print("           __")
    print("          /  \_ ")
    print("         /^    \ ")
    print("        /  ^    \_")
    print("      _/ ^ ^     ^\ ")
    print("     /  ^     ^    \ ")

# -----------

StepsRemaining = int(input("How far are we from the target? "))

for i in range(StepsRemaining, 0, -1):
    print(f"{i} steps remaining")

print("Target achieved!")

# -----------
NumberIsEven = False

while not NumberIsEven:
    brightness = int(input("What level of brightness is required?"))
    if brightness % 2 == 0:
        NumberIsEven = True
    else:
        print("Invalid input")

for i in range(2, brightness+2, 2):
    stars = i*"*"
    print(f"Brightness level: {stars}")

print("Complete")

# ------------

FavouriteWord = input("What word do you see? ")
print(FavouriteWord)
print("")
print("Displaying index positions...")
for i in range(0, len(FavouriteWord), 1):
    print(f"index {i}: {FavouriteWord[i]}")
print("Done!")

# -------------

ReverseWord = input("What word do you want to see in reverse? ")
print("")
print("Displaying phrase in reverse")
for i in range(len(ReverseWord)-1, -1, -1):
    print(ReverseWord[i], end="")

# --------------

