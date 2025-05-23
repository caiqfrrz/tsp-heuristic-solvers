# tsp-heuristic-solvers

**Authors:** Caique Ferraz and Guilherme Peruci

This repository contains a Python implementation of two heuristic algorithms for solving the Traveling Salesman Problem (TSP), developed for the Intelligent Systems class at UTFPR.

## Algorithms

- **Simulated Annealing**: A probabilistic technique that explores the solution space by accepting worse solutions with a decreasing probability, allowing escape from local minima.
- **Genetic Algorithm**: An evolutionary method that maintains a population of candidate solutions and applies selection, crossover, and mutation to evolve better routes.

## Features

- Simple and clear Python code for both algorithms
- Configurable parameters:
  - Temperature, cooling rate, and stopping criteria for Simulated Annealing
  - Population size, number of generations and mutation rates for the Genetic Algorithm

## Prerequisites

- Python 3.6+
- Standard libraries and matplotlib for visualization (requirements.txt)

## Installation

```bash
# Clone the repository
git clone https://github.com/caiqfrrz/tsp-heuristic-solvers.git
cd tsp-heuristic-solvers

# Install Python dependencies
pip install -r requirements.txt
```

## Usage

### Simulated annealing

Adjust parameters in the script or modify the function call:

```python
best_solution, best_cost, progress = simulated_annealing(
                                        cities,
                                        temperature,
                                        stopping_temperature=1e-3,
                                        alpha=0.995,
                                        time_budget=5.0
                                    )
```

### Genetic Algorithm

Adjust parameters:

```python
best_solution, best_cost, progress = genetic_algorithm(
                                        cities,
                                        population_size=100,
                                        generations=1000,
                                        mutation_rate=0.01,
                                        time_budget=5.0
                                    )
```
