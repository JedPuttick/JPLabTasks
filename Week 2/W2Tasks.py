
book = input("Whats your favourite genre of book? ")

if book.upper() == "ADVENTURE":
    print("I like adventure books!")

print("Finished reading book")

# -----------

activity = input("Please enter the activity to be performed: ")

if activity.upper() == "CALCULATE":
    print("Performing calculations...")
else:
    print("Performing activity")

print("Activity completed")

# ------------

direction = input("Input a direction (Up, Down, Left or Right): ")

if direction.upper() == "UP":
    print("Going up")
elif direction.upper() == "DOWN":
    print("Going down")
elif direction.upper() == "LEFT":
    print("Going left")
elif direction.upper() == "RIGHT":
    print("Going right")
else:
    print("Invalid direction")

# ----------
'''
number = int(input("Input a number: "))

if number % 2 > 0:
    print("Number is odd")
else:
    print("Number is even")

# ----------
'''
number2 = int(input("Input number 1: "))
number3 = int(input("Input number2: "))

if number2 > number3:
    print("Number 1 is bigger ")
else:
    print("Number 2 is bigger ")

# -----------

numbers = []
even = 0
odd = 0

for i in range(3):
    numbers.append(int(input("Input a number")))

for i in numbers:
    if i % 2 > 0:
        odd += 1
    else:
        even += 1

print(f"There were {odd} odd and {even} even numbers")

# --------