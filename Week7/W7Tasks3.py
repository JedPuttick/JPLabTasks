import json
file_path = "Week7/futurama.json"
def read(file_path):
    with open(file_path) as file:
        data = json.load(file)

    name = data["location"]
    population = data["population"]
    print(f"Place name: {name}")
    print(f"Population size: {population}")