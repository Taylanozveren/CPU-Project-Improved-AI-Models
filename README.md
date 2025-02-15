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

README.md → Project documentation and usage guide explaining all components.
requirements.txt → List of required Python dependencies such as NumPy, Pandas, and Matplotlib.
Dockerfile → Configuration file to containerize the project for consistent execution.
.github/workflows/ci.yml → GitHub Actions workflow for automated testing and CI/CD pipeline.
scheduler.py → Implements classical CPU scheduling algorithms like FCFS, Round Robin, Priority, SJF, and Preemptive Priority.
metrics.py → Provides functions to calculate performance metrics such as waiting time, turnaround time, and CPU utilization.
demo_algorithms.py → Demonstrates scheduling algorithms with sample data and generates Gantt chart visualizations.
optimizer.py → Implements Genetic Algorithm (GA) optimization for scheduling with both single-objective and multi-objective approaches.
advanced_ai.py → Introduces a Q-learning based Reinforcement Learning model to optimize scheduling dynamically.
main.py → The core script that executes all scheduling algorithms, AI-based optimizations, and logs the results.
results/ → A directory that stores CSV files containing performance evaluation data for analysis.


## ⚡ Installation  
```bash
### 1️⃣ **Clone the Repository**  


git clone https://github.com/Taylanozveren/CPU-Project-Improved-AI-Models.git
cd CPU-Project-Improved-AI-Models
2️⃣ Set Up a Virtual Environment (Recommended)
Windows:

python -m venv venv
venv\Scripts\activate
Linux/Mac:

python3 -m venv venv
source venv/bin/activate
3️⃣ Upgrade pip, setuptools, and wheel

venv\Scripts\python.exe -m pip install --upgrade pip setuptools wheel
4️⃣ Install Required Dependencies

pip install -r requirements.txt
🛠 Usage
Run the main script to execute scheduling algorithms, AI-based optimizations, and generate reports.


python main.py
📊 Expected Outputs:
Terminal Output: Displays scheduling orders, performance metrics, and comparisons.
Gantt Charts: Visual representations of scheduling execution.
CSV File Output: Results are saved in results/final_results.csv.
🐳 Docker Integration
To run the project inside a Docker container:

1️⃣ Build the Docker Image

docker build -t cpu_scheduler:latest .
2️⃣ Run the Container

docker run --rm cpu_scheduler:latest
🔄 Continuous Integration (CI)
GitHub Actions workflow (.github/workflows/ci.yml) automates dependency installation and testing on every push.
Ensures code stability by verifying scheduling algorithms and AI optimization models.
```


🚀 Future Enhancements
✅ Advanced Reinforcement Learning: Improve Q-learning models with deeper state-action space.
✅ Real-Time & Multi-Core Scheduling: Extend scheduling strategies to support multi-core CPU environments.
✅ Hybrid AI Models: Combine Genetic Algorithms & RL for intelligent process scheduling.
✅ Cloud Integration: Deploy as a cloud-based API for dynamic scheduling optimization.




