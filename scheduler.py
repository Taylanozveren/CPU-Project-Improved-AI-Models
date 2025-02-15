"""
scheduler.py

This module contains various CPU scheduling algorithms:
1. FCFS (First-Come, First-Served)
2. Round Robin
3. Non-preemptive Priority Scheduling
4. Shortest Job First (Non-preemptive)
5. Preemptive Priority Scheduling (NEW)
"""

from typing import List, Dict

def fcfs_schedule(processes: List[Dict]) -> List[tuple]:
    processes_sorted = sorted(processes, key=lambda p: p['arrival_time'])
    schedule = []
    current_time = 0
    for p in processes_sorted:
        if current_time < p['arrival_time']:
            current_time = p['arrival_time']
        start_time = current_time
        end_time = start_time + p['burst_time']
        schedule.append((p['id'], start_time, end_time))
        current_time = end_time
    return schedule

def round_robin_schedule(processes: List[Dict], time_quantum: int) -> List[tuple]:
    processes_sorted = sorted(processes, key=lambda p: p['arrival_time'])
    remaining_times = {p['id']: p['burst_time'] for p in processes_sorted}
    current_time = 0
    schedule = []
    queue = []
    index = 0
    while True:
        while index < len(processes_sorted) and processes_sorted[index]['arrival_time'] <= current_time:
            queue.append(processes_sorted[index])
            index += 1
        if not queue:
            if index < len(processes_sorted):
                current_time = processes_sorted[index]['arrival_time']
                continue
            else:
                break
        current_process = queue.pop(0)
        pid = current_process['id']
        start_time = current_time
        allocated_time = min(time_quantum, remaining_times[pid])
        current_time += allocated_time
        end_time = current_time
        schedule.append((pid, start_time, end_time))
        remaining_times[pid] -= allocated_time
        if remaining_times[pid] > 0:
            while index < len(processes_sorted) and processes_sorted[index]['arrival_time'] <= current_time:
                queue.append(processes_sorted[index])
                index += 1
            queue.append(current_process)
        if all(rt == 0 for rt in remaining_times.values()):
            break
    return schedule

def priority_schedule(processes: List[Dict]) -> List[tuple]:
    processes_sorted = sorted(processes, key=lambda p: p['arrival_time'])
    schedule = []
    current_time = 0
    completed = [False] * len(processes_sorted)
    count = 0
    while count < len(processes_sorted):
        available = [(i, p) for i, p in enumerate(processes_sorted)
                     if p['arrival_time'] <= current_time and not completed[i]]
        if not available:
            current_time = processes_sorted[count]['arrival_time']
            continue
        available.sort(key=lambda x: x[1]['priority'])
        i, chosen_proc = available[0]
        start_time = current_time
        end_time = start_time + chosen_proc['burst_time']
        schedule.append((chosen_proc['id'], start_time, end_time))
        current_time = end_time
        completed[i] = True
        count += 1
    return schedule

def sjf_schedule(processes: List[Dict]) -> List[tuple]:
    processes_sorted = sorted(processes, key=lambda p: p['arrival_time'])
    schedule = []
    current_time = 0
    completed = [False] * len(processes_sorted)
    count = 0
    while count < len(processes_sorted):
        available = [(i, p) for i, p in enumerate(processes_sorted)
                     if p['arrival_time'] <= current_time and not completed[i]]
        if not available:
            current_time = processes_sorted[count]['arrival_time']
            continue
        available.sort(key=lambda x: x[1]['burst_time'])
        i, chosen_proc = available[0]
        start_time = current_time
        end_time = start_time + chosen_proc['burst_time']
        schedule.append((chosen_proc['id'], start_time, end_time))
        current_time = end_time
        completed[i] = True
        count += 1
    return schedule

def preemptive_priority_schedule(processes: List[Dict]) -> List[tuple]:
    processes_sorted = sorted(processes, key=lambda p: p['arrival_time'])
    schedule = []
    current_time = 0
    remaining_times = {p['id']: p['burst_time'] for p in processes_sorted}
    arrived = []
    index = 0
    completed = 0
    total_processes = len(processes_sorted)
    while completed < total_processes:
        while index < total_processes and processes_sorted[index]['arrival_time'] <= current_time:
            arrived.append(processes_sorted[index])
            index += 1
        if not arrived:
            current_time = processes_sorted[index]['arrival_time']
            continue
        arrived.sort(key=lambda p: p['priority'])
        current_proc = arrived[0]
        start_time = current_time
        current_time += 1
        end_time = current_time
        schedule.append((current_proc['id'], start_time, end_time))
        remaining_times[current_proc['id']] -= 1
        if remaining_times[current_proc['id']] == 0:
            arrived.remove(current_proc)
            completed += 1
    return schedule
