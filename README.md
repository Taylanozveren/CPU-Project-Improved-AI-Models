# **TERM PROJECT (ADVANCED): AI-Enhanced CPU Scheduling and Optimization**  

**Author:** Taylan Özveren  
**Year:** 2025  

---

## 📌 Table of Contents  
- [Project Overview](#project-overview)  
- [Key Features](#key-features)  
- [Technical Approach](#technical-approach)  
- [Project Structure](#project-structure)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Docker Integration](#docker-integration)  
- [Continuous Integration (CI)](#continuous-integration-ci)  
- [Future Enhancements](#future-enhancements)  

---

## 🚀 Project Overview  

This project integrates **traditional CPU scheduling algorithms** with **Artificial Intelligence (AI) optimization techniques** to improve process scheduling in operating systems.  

It includes:  

✅ **Classical Scheduling Methods** (FCFS, Round Robin, Priority Scheduling, Shortest Job First).  
✅ **AI-Based Scheduling Enhancements** using **Genetic Algorithms (GA)** and **Reinforcement Learning (Q-learning)**.  
✅ **Data-Driven Performance Analysis**, including visualizations and performance metrics such as turnaround time, waiting time, and CPU utilization.  
✅ **Containerized Deployment** using **Docker** for consistent execution across environments.  
✅ **Automated Testing & CI/CD** using **GitHub Actions** to ensure reliability and performance.  

By combining **AI & optimization techniques**, this project enhances process scheduling strategies, making them **intelligent, adaptable, and efficient**.  

---

## 🔥 Key Features  

### ✅ **Traditional Scheduling Algorithms**  
- Implements **FCFS, Round Robin, Non-preemptive Priority, Preemptive Priority, and SJF**.  

### ✅ **AI Optimization with Genetic Algorithms (GA)**  
- **Single-objective GA:** Minimizes **average waiting time**.  
- **Multi-objective GA:** Balances **waiting time** and **turnaround time** using a **weighted optimization approach**.  

### ✅ **Reinforcement Learning (Q-learning) for Scheduling**  
- AI learns **optimal scheduling strategies** dynamically based on **reward-based learning**.  

### ✅ **Performance Visualization**  
- Generates **Gantt charts** to illustrate process execution.  

### ✅ **CSV-Based Result Logging**  
- Outputs performance metrics in CSV for further evaluation.  

### ✅ **Docker Integration**  
- Ensures **consistent execution** across different systems.  

### ✅ **Automated Testing & CI/CD**  
- GitHub Actions validates updates and prevents regressions.  

---

## 🤖 Technical Approach  

### 🔹 **Classical Scheduling Algorithms**  
This project implements various **traditional CPU scheduling techniques**, including:  

- **FCFS (First-Come, First-Served):** Executes processes in the order they arrive.  
- **Round Robin (RR):** Time-sliced execution for fair process scheduling.  
- **Non-Preemptive Priority Scheduling:** Processes execute based on priority.  
- **Preemptive Priority Scheduling:** Higher-priority processes can interrupt lower-priority processes.  
- **Shortest Job First (SJF):** Selects the shortest burst time for better efficiency.  

---

### 🔹 **AI-Based Optimization**  

#### 🧬 **Genetic Algorithm (GA) Optimization**  
- Uses **evolutionary techniques** to find the **optimal process execution order**.  
- Implements both **single-objective** (waiting time minimization) and **multi-objective** (balancing waiting & turnaround time).  

#### 🏆 **Reinforcement Learning (Q-learning) Optimization**  
- AI dynamically learns the best scheduling sequence.  
- The **Q-learning model** is trained to **reduce waiting time** through reward-based decision-making.  

---

### 🔹 **Performance Metrics & Analysis**  
- **Average Waiting Time:** Measures idle duration before process execution.  
- **Turnaround Time:** Measures total time from arrival to completion.  
- **CPU Utilization:** Evaluates efficiency of CPU usage.  
- **Throughput:** Calculates the number of completed processes per unit time.  
- **Gantt Charts:** Graphical representation of scheduling execution sequences.  

---

## 📂 Project Structure  

