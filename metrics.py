"""
metrics.py

Functions to calculate performance metrics.
"""

from typing import List, Tuple, Dict

def calculate_waiting_times(schedule: List[Tuple], processes: List[Dict]) -> Dict:
    waiting_times = {}
    burst_map = {p['id']: p['burst_time'] for p in processes}
    arrival_map = {p['id']: p['arrival_time'] for p in processes}
    for p in processes:
        pid = p['id']
        intervals = [interval for interval in schedule if interval[0] == pid]
        if not intervals:
            waiting_times[pid] = 0
            continue
        last_end_time = intervals[-1][2]
        total_time_in_system = last_end_time - arrival_map[pid]
        waiting_times[pid] = total_time_in_system - burst_map[pid]
    return waiting_times

def calculate_turnaround_times(schedule: List[Tuple], processes: List[Dict]) -> Dict:
    turnaround_times = {}
    arrival_map = {p['id']: p['arrival_time'] for p in processes}
    for p in processes:
        pid = p['id']
        intervals = [interval for interval in schedule if interval[0] == pid]
        if not intervals:
            turnaround_times[pid] = 0
            continue
        last_end_time = intervals[-1][2]
        turnaround_times[pid] = last_end_time - arrival_map[pid]
    return turnaround_times

def average_waiting_time(waiting_times: Dict) -> float:
    if len(waiting_times) == 0:
        return 0.0
    return sum(waiting_times.values()) / len(waiting_times)

def average_turnaround_time(turnaround_times: Dict) -> float:
    if len(turnaround_times) == 0:
        return 0.0
    return sum(turnaround_times.values()) / len(turnaround_times)

def cpu_utilization(schedule: List[Tuple]) -> float:
    if not schedule:
        return 0.0
    start_times = [s[1] for s in schedule]
    end_times = [s[2] for s in schedule]
    total_start = min(start_times)
    total_end = max(end_times)
    busy_time = sum([interval[2] - interval[1] for interval in schedule])
    total_time_span = total_end - total_start
    if total_time_span == 0:
        return 100.0
    return (busy_time / total_time_span) * 100

def throughput(schedule: List[Tuple], processes: List[Dict]) -> float:
    if not schedule or not processes:
        return 0.0
    start_times = [interval[1] for interval in schedule]
    end_times = [interval[2] for interval in schedule]
    total_start = min(start_times)
    total_end = max(end_times)
    total_time_span = total_end - total_start
    completed_processes = len(set([interval[0] for interval in schedule]))
    if total_time_span == 0:
        return float('inf')
    return completed_processes / total_time_span




if __name__ == "__main__":
    # Example usage
    processes = [
        {'id': 1, 'arrival_time': 0, 'burst_time': 5},
        {'id': 2, 'arrival_time': 1, 'burst_time': 3},
        {'id': 3, 'arrival_time': 2, 'burst_time': 8},
        {'id': 4, 'arrival_time': 3, 'burst_time': 6}
    ]
    schedule = [
        (1, 0, 5),  # (process_id, start_time, end_time)
        (2, 5, 8),
        (3, 8, 16),
        (4, 16, 22)
    ]

    w_times = calculate_waiting_times(schedule, processes)
    t_times = calculate_turnaround_times(schedule, processes)
    avg_wt = average_waiting_time(w_times)
    avg_tat = average_turnaround_time(t_times)
    cpu_util = cpu_utilization(schedule)
    thpt = throughput(schedule, processes)

    print("Waiting times:", w_times)
    print("Turnaround times:", t_times)
    print("Average waiting time:", avg_wt)
    print("Average turnaround time:", avg_tat)
    print("CPU utilization:", cpu_util)
    print("Throughput:", thpt)