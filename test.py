import random
import time
import matplotlib.pyplot as plt  # Import matplotlib for plotting
from genetic import genetic_algorithm
from sim_anneal import simulated_annealing

def plot_convergence_curve(sa_progress, ga_progress):
    """Plots the convergence curve (Cost vs. Time) for both algorithms."""
    sa_times, sa_costs = zip(*sa_progress)
    ga_times, ga_costs = zip(*ga_progress)

    plt.figure(figsize=(10, 6))
    plt.plot(sa_times, sa_costs, label="Simulated Annealing", color="blue")
    plt.plot(ga_times, ga_costs, label="Genetic Algorithm", color="green")
    plt.title("Convergence Curve (Cost vs. Time)")
    plt.xlabel("Elapsed Time (seconds)")
    plt.ylabel("Best Cost")
    plt.legend()
    plt.grid()
    plt.show()

def test_anneal(cities):
    start = time.perf_counter()
    route, cost, progress = simulated_annealing(cities, 1000, time_budget=10.0)
    elapsed = time.perf_counter() - start

    print("=== Simulated Annealing ===")
    print("Melhor rota:", route)
    print(f"Custo total: {cost:.2f}")
    print(f"Tempo de execução: {elapsed:.3f} segundos\n")

    return progress

def test_genetic(cities):
    start = time.perf_counter()
    best_route, best_length, progress = genetic_algorithm(cities, time_budget=10.0)
    elapsed = time.perf_counter() - start

    print("=== Genetic Algorithm ===")
    print("Melhor rota encontrada:", best_route)
    print(f"Comprimento total: {best_length:.2f}")
    print(f"Tempo de execução: {elapsed:.3f} segundos\n")

    return progress

if __name__ == "__main__":
    cities = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(100)]
    sa_progress = test_anneal(cities)
    ga_progress = test_genetic(cities)
    plot_convergence_curve(sa_progress, ga_progress)