"""
main.py

Combines scheduling demos, GA optimization, and RL approach.
Saves results to CSV in the results/ folder.
"""

import os
import pandas as pd
from demo_algorithms import demo
from optimizer import run_genetic_algorithm
from advanced_ai import q_learning_scheduler
from scheduler import fcfs_schedule
from metrics import (
    calculate_waiting_times,
    calculate_turnaround_times,
    average_waiting_time,
    average_turnaround_time
)

def main():
    print("=== ACM369 TERM PROJECT (ADVANCED) ===")
    print("Title: Processes Tasks + AI (Genetic Algorithms & Reinforcement Learning)")
    print("Author: Taylan Özveren\n")
    
    # Part 1: Demonstration of standard algorithms
    print("Part 1: Demonstrating standard CPU scheduling algorithms...\n")
    demo()
    
    # Part 2: GA (Single-objective)
    print("\nPart 2: Genetic Algorithm (Single Objective: Minimize Avg Waiting Time)\n")
    processes = [
        {'id': 1, 'arrival_time': 0, 'burst_time': 4, 'priority': 2},
        {'id': 2, 'arrival_time': 1, 'burst_time': 3, 'priority': 1},
        {'id': 3, 'arrival_time': 2, 'burst_time': 2, 'priority': 3},
        {'id': 4, 'arrival_time': 3, 'burst_time': 5, 'priority': 2},
    ]
    best_individual, best_fitness = run_genetic_algorithm(processes, pop_size=10, generations=20, mutation_rate=0.1)
    print(f"Best individual (GA Single-objective): {best_individual}")
    print(f"Fitness (negative avg waiting time): {best_fitness}\n")
    forced_processes = []
    for pid in best_individual:
        for p in processes:
            if p['id'] == pid:
                forced_processes.append({'id': p['id'], 'arrival_time': 0, 'burst_time': p['burst_time']})
                break
    final_schedule = fcfs_schedule(forced_processes)
    wt = calculate_waiting_times(final_schedule, forced_processes)
    print("Final schedule (forced FCFS in GA order):", final_schedule)
    print("Final average waiting time:", average_waiting_time(wt))
    
    # Part 3: GA (Multi-objective)
    print("\nPart 3: Genetic Algorithm (Multi-objective: Weighted WT & TAT)\n")
    best_individual_mo, best_fit_mo = run_genetic_algorithm(
        processes, 
        pop_size=10, 
        generations=20, 
        mutation_rate=0.1, 
        objective="multi",
        w1=0.7,
        w2=0.3
    )
    print(f"Best individual (GA Multi-objective): {best_individual_mo}")
    print(f"Fitness (negative weighted sum): {best_fit_mo}\n")
    forced_processes_mo = []
    for pid in best_individual_mo:
        for p in processes:
            if p['id'] == pid:
                forced_processes_mo.append({'id': p['id'], 'arrival_time': 0, 'burst_time': p['burst_time']})
                break
    final_schedule_mo = fcfs_schedule(forced_processes_mo)
    wt_mo = calculate_waiting_times(final_schedule_mo, forced_processes_mo)
    tat_mo = calculate_turnaround_times(final_schedule_mo, forced_processes_mo)
    print("Final schedule (Multi-objective GA order):", final_schedule_mo)
    print("Avg waiting time:", average_waiting_time(wt_mo))
    print("Avg turnaround time:", average_turnaround_time(tat_mo))
    
    # Part 4: RL (Q-learning)
    print("\nPart 4: Reinforcement Learning (Q-learning) Approach\n")
    rl_schedule = q_learning_scheduler(processes, episodes=50)
    print("RL-derived order of processes:", rl_schedule)
    forced_processes_rl = []
    for pid in rl_schedule:
        for p in processes:
            if p['id'] == pid:
                forced_processes_rl.append({'id': p['id'], 'arrival_time': 0, 'burst_time': p['burst_time']})
                break
    final_schedule_rl = fcfs_schedule(forced_processes_rl)
    wt_rl = calculate_waiting_times(final_schedule_rl, forced_processes_rl)
    print("Final schedule (RL forced FCFS order):", final_schedule_rl)
    print("Avg waiting time:", average_waiting_time(wt_rl))
    
    # Save results to CSV
    os.makedirs("results", exist_ok=True)
    df = pd.DataFrame({
        "Algorithm": ["GA_Single", "GA_Multi", "RL"],
        "Schedule": [str(best_individual), str(best_individual_mo), str(rl_schedule)],
        "AvgWaitingTime": [
            average_waiting_time(wt),
            average_waiting_time(wt_mo),
            average_waiting_time(wt_rl)
        ]
    })
    df.to_csv("results/final_results.csv", index=False)
    print("\nResults saved to results/final_results.csv")

if __name__ == "__main__":
    main()
