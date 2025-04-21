import math
import random

from utils import calculate_total_distance

def initial_solution(cities):
    n = len(cities)
    solution = list(range(n))
    random.shuffle(solution)
    return solution

def simulated_annealing(cities, temperature, stopping_temperature=1e-3, alpha=0.995):
    n = len(cities)
    current_solution = initial_solution(cities)
    current_cost = calculate_total_distance(cities, current_solution)
    best_solution = current_solution[:]
    best_cost = current_cost

    while temperature > stopping_temperature:
        candidate_solution = current_solution[:]
        i, j = random.sample(range(n), 2)
        candidate_solution[i : j+1] = reversed(candidate_solution[i : j+1])
        candidate_cost = calculate_total_distance(cities, candidate_solution)

        delta_cost = candidate_cost - current_cost
        if delta_cost < 0 or math.exp(-delta_cost / temperature) > random.random():
            current_solution = candidate_solution
            current_cost = candidate_cost

            if current_cost < best_cost:
                best_solution = current_solution[:]
                best_cost = current_cost

        temperature *= alpha

    return best_solution, best_cost
