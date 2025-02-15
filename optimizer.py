"""
optimizer.py

Implements Genetic Algorithm (GA) approaches for scheduling optimization.
1) Single-objective GA (minimize average waiting time).
2) Multi-objective GA (weighted sum of waiting time and turnaround time).
"""

import random
import numpy as np
from typing import List, Dict
from scheduler import fcfs_schedule
from metrics import (
    calculate_waiting_times,
    calculate_turnaround_times,
    average_waiting_time,
    average_turnaround_time
)

def generate_random_population(process_ids: List[int], pop_size: int) -> List[List[int]]:
    population = []
    for _ in range(pop_size):
        individual = process_ids[:]
        random.shuffle(individual)
        population.append(individual)
    return population

def single_objective_fitness(individual: List[int], processes: List[Dict]) -> float:
    ordered_processes = []
    for pid in individual:
        for p in processes:
            if p['id'] == pid:
                ordered_processes.append({'id': p['id'], 'arrival_time': 0, 'burst_time': p['burst_time']})
                break
    schedule = fcfs_schedule(ordered_processes)
    w_times = calculate_waiting_times(schedule, ordered_processes)
    avg_wt = average_waiting_time(w_times)
    return -avg_wt

def multi_objective_fitness(individual: List[int], processes: List[Dict], w1=0.5, w2=0.5) -> float:
    ordered_processes = []
    for pid in individual:
        for p in processes:
            if p['id'] == pid:
                ordered_processes.append({'id': p['id'], 'arrival_time': 0, 'burst_time': p['burst_time']})
                break
    schedule = fcfs_schedule(ordered_processes)
    w_times = calculate_waiting_times(schedule, ordered_processes)
    t_times = calculate_turnaround_times(schedule, ordered_processes)
    avg_wt = average_waiting_time(w_times)
    avg_tat = average_turnaround_time(t_times)
    combined = w1 * avg_wt + w2 * avg_tat
    return -combined

def selection(population: List[List[int]], fitness_scores: List[float], num_parents: int) -> List[List[int]]:
    sorted_pop = sorted(zip(population, fitness_scores), key=lambda x: x[1], reverse=True)
    parents = [ind for ind, score in sorted_pop[:num_parents]]
    return parents

def crossover(parent1: List[int], parent2: List[int]) -> List[int]:
    point = random.randint(1, len(parent1) - 1)
    child = parent1[:point]
    for gene in parent2:
        if gene not in child:
            child.append(gene)
    return child

def mutate(individual: List[int], mutation_rate: float):
    if random.random() < mutation_rate:
        idx1 = random.randint(0, len(individual) - 1)
        idx2 = random.randint(0, len(individual) - 1)
        individual[idx1], individual[idx2] = individual[idx2], individual[idx1]

def run_genetic_algorithm(processes: List[Dict], pop_size=10, generations=20, mutation_rate=0.1, objective="single", w1=0.5, w2=0.5):
    process_ids = [p['id'] for p in processes]
    population = generate_random_population(process_ids, pop_size)
    for _ in range(generations):
        if objective == "single":
            fitness_scores = [single_objective_fitness(ind, processes) for ind in population]
        else:
            fitness_scores = [multi_objective_fitness(ind, processes, w1, w2) for ind in population]
        parents = selection(population, fitness_scores, num_parents=2)
        new_population = []
        while len(new_population) < pop_size:
            parent1 = random.choice(parents)
            parent2 = random.choice(parents)
            child = crossover(parent1, parent2)
            mutate(child, mutation_rate)
            new_population.append(child)
        population = new_population
    if objective == "single":
        final_fitness_scores = [single_objective_fitness(ind, processes) for ind in population]
    else:
        final_fitness_scores = [multi_objective_fitness(ind, processes, w1, w2) for ind in population]
    best_index = np.argmax(final_fitness_scores)
    best_individual = population[best_index]
    return best_individual, final_fitness_scores[best_index]


if __name__ == "__main__":
    processes = [
        {'id': 1, 'burst_time': 5},
        {'id': 2, 'burst_time': 3},
        {'id': 3, 'burst_time': 8},
        {'id': 4, 'burst_time': 6}
    ]
    best_individual, best_fitness = run_genetic_algorithm(processes, pop_size=10, generations=20, mutation_rate=0.1, objective="single")
    print("Best individual:", best_individual)
    print("Best fitness score:", best_fitness)