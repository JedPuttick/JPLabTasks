def likelihood():
    likelihoods = (50, 38, 27, 99, 4)
    smallest = likelihoods[0]
    for l in likelihoods:
        if l < smallest:
            smallest = l
    return smallest

def run_task1():
    BestPlace = likelihood()
    print(f"Minimum likelihood of falling: {BestPlace}%")

run_task1()

# ---------

def likelihood_min_max():
    likelihoods = (50, 38, 27, 99, 4)
    smallest = likelihoods[0]
    biggest = likelihoods[0]
    for i in likelihoods:
        if i < smallest:
            smallest = i
        if i > biggest:
            biggest = i
    return (smallest, biggest)
