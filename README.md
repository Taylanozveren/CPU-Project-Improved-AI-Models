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

This project integrates advanced CPU scheduling algorithms with modern AI techniques to optimize process management. It combines traditional scheduling methods with Genetic Algorithms (GA) for both single-objective and multi-objective optimization, and a basic Q-learning approach for reinforcement learning.

---

## Key Features

- **Comprehensive Scheduling:** Implements classical algorithms (FCFS, Round Robin, Priority, SJF, Preemptive Priority) for CPU scheduling.
- **AI Optimization:** Utilizes Genetic Algorithms and Q-learning to optimize scheduling performance.
- **Data Visualization:** Generates Gantt charts and other visual outputs using Matplotlib.
- **Modern DevOps Practices:** Includes Docker containerization and GitHub Actions for continuous integration.
- **Result Logging:** Outputs simulation results to CSV files for further analysis.

---

## Project Structure

- **README.md:** This documentation file describing the project, its features, and usage instructions.
- **requirements.txt:** Lists the Python dependencies (matplotlib, numpy, pandas) required for the project.
- **Dockerfile:** Contains instructions to build a Docker image for containerized deployment.
- **.github/workflows/ci.yml:** Defines a GitHub Actions workflow for automated testing and CI/CD.
- **scheduler.py:** Implements CPU scheduling algorithms such as FCFS, Round Robin, Priority, SJF, and Preemptive Priority in a concise manner.
- **metrics.py:** Provides functions to calculate performance metrics like waiting time, turnaround time, CPU utilization, and throughput.
- **demo_algorithms.py:** Demonstrates the scheduling algorithms and generates Gantt chart visualizations.
- **optimizer.py:** Contains implementations of Genetic Algorithms for both single-objective and multi-objective scheduling optimization.
- **advanced_ai.py:** Offers a basic Q-learning example to optimize process scheduling using reinforcement learning.
- **main.py:** Serves as the entry point to run demonstrations, perform GA and RL optimizations, and save simulation results.
- **results/**: A folder designated for storing output CSV files with simulation results.

---

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Taylanozveren/CPU-Project-Improved-AI-Models.git
   cd CPU-Project-Improved-AI-Models
```bash


A.)
   ```bash
python -m venv venv
venv\Scripts\activate


B.)
venv\Scripts\python.exe -m pip install --upgrade pip setuptools wheel


C.)
pip install -r requirements.txt


D.)
python main.py
```

Docker Integration
To run the project within a Docker container:

Build the Docker Image:

docker build -t cpu_scheduler:latest .

Run the Docker Container:

docker run --rm cpu_scheduler:latest

Continuous Integration (CI)
A GitHub Actions workflow is set up in .github/workflows/ci.yml to automatically install dependencies and run the main script on every push or pull request, ensuring continuous integration and testing.

Future Enhancements
Enhanced RL Models: Extend the Q-learning framework with more sophisticated state representations and realistic scheduling scenarios.
Additional Metrics: Integrate further performance metrics like CPU utilization, throughput, and energy efficiency.
Real-Time and Multi-Core Scheduling: Adapt algorithms for real-time constraints and multi-core environments.
Hybrid Approaches: Explore combinations of GA and RL for improved scheduling optimization.

This README provides a comprehensive yet concise overview of the project, its features, structure, and usage, tailored for technical and AI/Data Science audiences.
