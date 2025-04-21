import random
from genetic import genetic_algorithm
from sim_anneal import simulated_annealing

def test_anneal(cities):
    route, cost = simulated_annealing(cities, 1000)
    print("Melhor rota:", route)
    print(f"Custo total: {cost:.2f}")

def test_genetic(cities):
    best_route, best_length = genetic_algorithm(
        cities,
    )
    print("Melhor rota encontrada:", best_route)
    print(f"Comprimento total: {best_length:.2f}")

if __name__ == "__main__":
    cities = [(random.uniform(0,100), random.uniform(0,100)) for _ in range(12)]
    test_genetic(cities)
    test_anneal(cities)