"""
advanced_ai.py

A simple example of Reinforcement Learning (Q-learning) for scheduling.
This is highly simplified and mostly for demonstration purposes.

We define a tiny environment:
- State: (tuple of remaining process IDs, current time)
- Action: choose next process
- Reward: negative waiting time (heuristic)

This is just a conceptual skeleton.
"""

import random
import numpy as np
from typing import List, Dict

class RLSchedulerEnv:
    def __init__(self, processes: List[Dict]):
        self.processes = processes
        self.remaining = [p['id'] for p in processes]
        self.burst_map = {p['id']: p['burst_time'] for p in processes}
        self.current_time = 0
        self.done = False
    
    def reset(self):
        self.remaining = [p['id'] for p in self.processes]
        self.current_time = 0
        self.done = False
        return self._get_state()
    
    def _get_state(self):
        return (tuple(self.remaining), self.current_time)
    
    def step(self, action_pid):
        if action_pid not in self.remaining:
            return self._get_state(), -100.0, self.done
        burst = self.burst_map[action_pid]
        start_time = self.current_time
        self.current_time += burst
        end_time = self.current_time
        self.remaining.remove(action_pid)
        waiting_time = start_time  # arrival_time = 0 assumed
        reward = -float(waiting_time)
        if len(self.remaining) == 0:
            self.done = True
        return self._get_state(), reward, self.done

def q_learning_scheduler(processes: List[Dict], episodes=50, alpha=0.1, gamma=0.9, epsilon=0.1):
    env = RLSchedulerEnv(processes)
    Q = {}
    
    def get_Q(state, action):
        return Q.get((state, action), 0.0)
    
    for _ in range(episodes):
        state = env.reset()
        done = False
        while not done:
            possible_actions = list(state[0])
            if random.random() < epsilon:
                action = random.choice(possible_actions)
            else:
                qvals = [get_Q(state, a) for a in possible_actions]
                max_q = max(qvals)
                best_actions = [a for a, qv in zip(possible_actions, qvals) if qv == max_q]
                action = random.choice(best_actions)
            next_state, reward, done = env.step(action)
            old_q = get_Q(state, action)
            if not done:
                next_actions = list(next_state[0])
                future_qs = [get_Q(next_state, a) for a in next_actions]
                max_future_q = max(future_qs) if future_qs else 0
                new_q = old_q + alpha * (reward + gamma * max_future_q - old_q)
            else:
                new_q = old_q + alpha * (reward - old_q)
            Q[(state, action)] = new_q
            state = next_state
    schedule = []
    state = env.reset()
    done = False
    while not done:
        possible_actions = list(state[0])
        qvals = [get_Q(state, a) for a in possible_actions]
        max_q = max(qvals)
        best_actions = [a for a, qv in zip(possible_actions, qvals) if qv == max_q]
        action = random.choice(best_actions)
        next_state, reward, done = env.step(action)
        schedule.append(action)
        state = next_state
    return schedule


if __name__ == "__main__":
    processes = [
        {'id': 1, 'burst_time': 5},
        {'id': 2, 'burst_time': 3},
        {'id': 3, 'burst_time': 8},
        {'id': 4, 'burst_time': 6}
    ]
    schedule = q_learning_scheduler(processes, episodes=50, alpha=0.1, gamma=0.9, epsilon=0.1)
    print("Scheduled order of processes:", schedule)