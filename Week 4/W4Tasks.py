print("Program started")
CharInput = input("Please enter a standard character: ")
if len(CharInput) == 1:
    ASCII = ord(CharInput)
    print(f"The ASCII code for {CharInput} is {ASCII}")
else:
    print("Not a single character")
print("Program ended")

# -------
InRange = False
print("Program started")
ASCII = abs(int(input("Please enter an ASCII code: ")))
for i in range(32, 127, 1):
    if i == ASCII:
        print(f"The character represented by code {ASCII} is {chr(ASCII)}")
        InRange = True

if not InRange:
    print("Character not in printable range")

print("Program ended!")