# TERM PROJECT (ADVANCED): Processes Tasks and Implementations with AI Enhancements

**Author:** Taylan Özveren  
**Year:** 2025

---

## Table of Contents

- [Project Overview](#project-overview)
- [Key Features](#key-features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Docker Integration](#docker-integration)
- [Continuous Integration (CI)](#continuous-integration-ci)
- [Future Enhancements](#future-enhancements)


---

## Project Overview

This project demonstrates a cutting-edge integration of classical CPU scheduling algorithms with modern Artificial Intelligence techniques. It is designed to optimize process management by combining:

- **Traditional OS Scheduling Algorithms:**  
  Implementations of FCFS (First-Come, First-Served), Round Robin, Priority Scheduling (both non-preemptive and preemptive), and Shortest Job First (SJF).

- **Genetic Algorithms (GA):**  
  Both single-objective (minimizing average waiting time) and multi-objective (optimizing a weighted sum of waiting time and turnaround time) approaches are used to determine the optimal process scheduling order.

- **Reinforcement Learning (Q-learning):**  
  A basic Q-learning framework is employed to explore and optimize the process execution order.

The project is implemented in Python using key libraries such as NumPy, Matplotlib, and Pandas. It also integrates modern software practices including Docker for containerization and GitHub Actions for Continuous Integration (CI).

---

## Key Features

- **Comprehensive Scheduling Algorithms:**  
  Implements both classical (FCFS, Round Robin, Priority, SJF) and advanced preemptive scheduling methods.

- **AI-Based Optimization:**  
  Demonstrates the use of Genetic Algorithms (single and multi-objective) and Reinforcement Learning (Q-learning) to optimize scheduling performance.

- **Data Visualization:**  
  Utilizes Matplotlib to generate Gantt charts and other visual outputs for algorithm performance analysis.

- **Modern DevOps Practices:**  
  - **Docker:** Containerizes the application for consistent deployment.
  - **GitHub Actions:** Provides CI/CD configuration to automatically run tests on code pushes.

- **Result Logging:**  
  Saves simulation results (e.g., average waiting times) in CSV format for further analysis.

---

## Project Structure

cpu_scheduler_project/ ├─ README.md # This detailed project documentation. ├─ requirements.txt # Python dependencies: matplotlib, numpy, pandas. ├─ Dockerfile # Docker configuration for containerization. ├─ .github/ │ └─ workflows/ │ └─ ci.yml # GitHub Actions workflow for CI/CD. ├─ scheduler.py # Implementation of CPU scheduling algorithms. ├─ metrics.py # Functions to calculate performance metrics. ├─ demo_algorithms.py # Script for demonstrating scheduling algorithms and visualizations. ├─ optimizer.py # Genetic Algorithm implementations for scheduling optimization. ├─ advanced_ai.py # Q-learning based Reinforcement Learning demonstration. ├─ main.py # Main script orchestrating demos, GA, RL, and result logging. └─ results/ # Folder for output CSV files containing simulation results.

