import random
import math

from utils import calculate_total_distance

def initial_population(population_size, n):
    population = []
    for _ in range(population_size):
        solution = list(range(n))
        random.shuffle(solution)
        population.append(solution)
    return population

def tournment_selection(population, cities, k=3):
    selected =  random.sample(population, k)
    return min(selected, key=lambda x: calculate_total_distance(cities, x))

def crossover(parent1, parent2):
    n = len(parent1)
    split = random.randint(0, n-1)
    child = parent1[:split] + [city for city in parent2 if city not in parent1[:split]]
    return child

def mutate(route, mutation_rate):
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(route)), 2)
        route[i], route[j] = route[j], route[i]

def genetic_algorithm(cities, population_size=100, generations=1000, mutation_rate=0.01):
    n = len(cities)
    population = initial_population(population_size, n)

    best = min(population, key=lambda x: calculate_total_distance(cities, x))
    best_cost = calculate_total_distance(cities, best)

    for gen in range(generations):
        new_population = []
        population_sorted = sorted(population, key=lambda x: calculate_total_distance(cities, x))
        new_population.extend(population_sorted[:2])

        while len(new_population) < population_size:
            p1 = tournment_selection(population, cities)
            p2 = tournment_selection(population, cities)

            if random.random() < 0.9:
                c1 = crossover(p1, p2)
                c2 = crossover(p2, p1)
            else:
                c1 = p1[:]
                c2 = p2[:]
            mutate(c1, mutation_rate)
            mutate(c2, mutation_rate)
            new_population += [c1, c2]
        
        population = new_population
        current_best = min(population, key=lambda x: calculate_total_distance(cities, x))
        current_cost = calculate_total_distance(cities, current_best)
        
        if current_cost < best_cost:
            best = current_best
            best_cost = current_cost

    return best, best_cost
