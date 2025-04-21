import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def calculate_total_distance(cities, solution):
    total_distance = 0
    for i in range(len(solution)):
        city1 = cities[solution[i]]
        city2 = cities[solution[(i + 1) % len(solution)]]
        total_distance += calculate_distance(city1, city2)
    return total_distance