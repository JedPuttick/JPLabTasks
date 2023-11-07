def observed():
    observations = {"Car", "Sky Scraper", "Sky Scraper", "Bike", "House", "House"}
    return observations


def run_task1():
    o = observed()
    print(o)


run_task1()


# ----------

def observed_items():
    observations = []
    for i in range(0, 7):
        observations.append(input("What can you see? "))
    return observations


def run_task2():
    print("Counting observations...")
    obs = observed_items()
    observationsSet = set()
    for observation in obs:
        observationTuple = (observation, obs.count(observation))
        observationsSet.add(observationTuple)
    for observationTuple in observationsSet:
        print(f"{observationTuple[0]} seen {observationTuple[1]} times")


run_task2()

# ----------

