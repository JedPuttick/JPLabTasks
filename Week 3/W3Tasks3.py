rows = int(input("How many rows? "))
columns = int(input("How many columns? "))

print("Here I go: ")

for i in range(rows):
    for j in range(columns):
        print(":-)", end="")
    print("")

print("Done!")

# -------------

MarkText = input("Please enter a sequence: ")
Marker = input("Please enter the marker character: ")
InteriorString = ""

for i in range(len(MarkText)):
    if MarkText[i] == Marker:
        a = i+1
        InteriorString.add(MarkText[i])
        while MarkText[a] != Marker:
            InteriorString.add(a)

print(InteriorString)