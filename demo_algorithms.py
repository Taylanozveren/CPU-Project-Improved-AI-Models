"""
demo_algorithms.py

Demonstrates scheduling algorithms with small sets of processes, including Gantt charts.
"""

import matplotlib.pyplot as plt
from typing import List, Dict
from scheduler import (
    fcfs_schedule,
    round_robin_schedule,
    priority_schedule,
    sjf_schedule,
    preemptive_priority_schedule
)
from metrics import (
    calculate_waiting_times,
    calculate_turnaround_times,
    average_waiting_time,
    average_turnaround_time,
    cpu_utilization,
    throughput
)

def generate_gantt_chart(schedule, title):
    fig, ax = plt.subplots()
    color_map = {}
    color_cycle = plt.cm.get_cmap('hsv', len(set([s[0] for s in schedule])) + 1)
    unique_pids = list(set([s[0] for s in schedule]))
    for i, pid in enumerate(unique_pids):
        color_map[pid] = color_cycle(i)
    for interval in schedule:
        pid, start, end = interval
        ax.barh(y=pid, width=end - start, left=start, height=0.5,
                color=color_map[pid], edgecolor='black')
        ax.text(x=(start + end) / 2, y=pid, s=f"P{pid}", va='center', ha='center', color='white')
    ax.set_xlabel("Time")
    ax.set_ylabel("Process ID")
    ax.set_title(title)
    plt.tight_layout()
    plt.show()

def demo():
    processes = [
        {'id': 1, 'arrival_time': 0, 'burst_time': 4, 'priority': 2},
        {'id': 2, 'arrival_time': 1, 'burst_time': 3, 'priority': 1},
        {'id': 3, 'arrival_time': 2, 'burst_time': 2, 'priority': 3},
        {'id': 4, 'arrival_time': 3, 'burst_time': 5, 'priority': 2},
    ]
    
    print("=== DEMO OF SCHEDULING ALGORITHMS ===")
    
    # FCFS
    fcfs_result = fcfs_schedule(processes)
    print("\nFCFS Schedule:", fcfs_result)
    wt = calculate_waiting_times(fcfs_result, processes)
    tat = calculate_turnaround_times(fcfs_result, processes)
    print("FCFS Avg Waiting Time:", average_waiting_time(wt))
    print("FCFS Avg Turnaround Time:", average_turnaround_time(tat))
    generate_gantt_chart(fcfs_result, "FCFS Gantt Chart")
    
    # Round Robin
    rr_result = round_robin_schedule(processes, time_quantum=2)
    print("\nRound Robin Schedule:", rr_result)
    wt = calculate_waiting_times(rr_result, processes)
    tat = calculate_turnaround_times(rr_result, processes)
    print("RR Avg Waiting Time:", average_waiting_time(wt))
    print("RR Avg Turnaround Time:", average_turnaround_time(tat))
    generate_gantt_chart(rr_result, "Round Robin Gantt Chart")
    
    # Non-preemptive Priority
    prio_result = priority_schedule(processes)
    print("\nNon-preemptive Priority Schedule:", prio_result)
    wt = calculate_waiting_times(prio_result, processes)
    tat = calculate_turnaround_times(prio_result, processes)
    print("Priority Avg Waiting Time:", average_waiting_time(wt))
    print("Priority Avg Turnaround Time:", average_turnaround_time(tat))
    generate_gantt_chart(prio_result, "Priority Gantt Chart")
    
    # SJF
    sjf_result = sjf_schedule(processes)
    print("\nSJF Schedule:", sjf_result)
    wt = calculate_waiting_times(sjf_result, processes)
    tat = calculate_turnaround_times(sjf_result, processes)
    print("SJF Avg Waiting Time:", average_waiting_time(wt))
    print("SJF Avg Turnaround Time:", average_turnaround_time(tat))
    generate_gantt_chart(sjf_result, "SJF Gantt Chart")
    
    # Preemptive Priority
    pprio_result = preemptive_priority_schedule(processes)
    print("\nPreemptive Priority Schedule:", pprio_result)
    wt = calculate_waiting_times(pprio_result, processes)
    tat = calculate_turnaround_times(pprio_result, processes)
    print("Preemptive Priority Avg Waiting Time:", average_waiting_time(wt))
    print("Preemptive Priority Avg Turnaround Time:", average_turnaround_time(tat))
    generate_gantt_chart(pprio_result, "Preemptive Priority Gantt Chart")

if __name__ == "__main__":
    demo()
