i = 0

loops = int(input("How many apples should I remove? "))
while i < loops:
    print("Removed apple.")
    i += 1

# ------------

j = 1
obstacles = int(input("How many obstacles should I avoid? "))

while j < obstacles+1:
    print("Avoiding...")
    print(f"...Done! {j} obstacles avoided.")
    j+=1

print("All obstacles have been avoided")

# ------------

x = 1
bars = int(input("How many bars should be charged"))

while x < bars+1:
    bar = "█"
    visibleBars = x*bar
    print(f"Charging: {visibleBars}")
    x+=1

print("The battery is fully charged")