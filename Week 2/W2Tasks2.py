CoverType = input("Input a cover type: ")

if CoverType.upper() == "HARD":
    print("Books with hard covers can be more expensive")
elif CoverType.upper() == "SOFT":
    PerfectBound = input("Is the book perfect bound ?")
    if PerfectBound.upper() == "YES":
        print("Soft covers with coils or stitches are great for short books")
else:
    print("Invalid cover type")

# ---------

