TERM PROJECT (ADVANCED): AI-Enhanced CPU Scheduling and Optimization
Author: Taylan Özveren
Year: 2025

📌 Table of Contents
Project Overview
Key Features
Technical Approach
Project Structure
Installation
Usage
Docker Integration
Continuous Integration (CI)
Future Enhancements
🚀 Project Overview
This project combines traditional CPU scheduling algorithms with Artificial Intelligence (AI) optimization techniques to improve process scheduling in operating systems. The implementation includes:

Classical Scheduling Methods (e.g., FCFS, Round Robin, Priority Scheduling, Shortest Job First).
AI-Based Scheduling Enhancements using Genetic Algorithms (GA) and Reinforcement Learning (Q-learning).
Data-Driven Performance Analysis, including visualizations and performance metrics (e.g., turnaround time, waiting time, CPU utilization).
Containerized Deployment using Docker for easy execution and compatibility.
Automated Testing & CI/CD using GitHub Actions to ensure reliability.
By leveraging AI & optimization techniques, this project aims to enhance process scheduling strategies in an intelligent, adaptable, and efficient manner.

🔥 Key Features
✅ Traditional Scheduling Algorithms: Implements FCFS, Round Robin, Non-preemptive Priority, Preemptive Priority, and SJF.
✅ AI Optimization with Genetic Algorithms (GA): Uses single-objective (minimizing waiting time) and multi-objective (optimizing waiting + turnaround time).
✅ Reinforcement Learning (Q-learning) for Scheduling: AI learns to optimize scheduling order dynamically.
✅ Visual Performance Analysis: Generates Gantt charts to visualize process execution.
✅ CSV-Based Result Logging: Performance metrics are stored in CSV for further evaluation.
✅ Docker Integration: Containerized execution ensures a consistent environment across different systems.
✅ Automated Testing & CI/CD: GitHub Actions validates updates and prevents regressions.

🤖 Technical Approach
This project integrates traditional operating system scheduling with modern AI techniques:

🔹 Classical Scheduling Algorithms
These are implemented as baseline comparisons:

FCFS (First-Come, First-Served): Simple queue-based execution.
Round Robin (RR): Time-sliced execution for fairness.
Non-Preemptive Priority Scheduling: Processes execute based on priority levels.
Preemptive Priority Scheduling: Higher-priority processes preempt running processes.
Shortest Job First (SJF): Selects the shortest burst time for efficiency.
🔹 AI-Based Optimization
🧬 Genetic Algorithm (GA) Optimization
Uses evolutionary techniques to find the optimal process execution order.
Single-objective GA: Minimizes average waiting time.
Multi-objective GA: Balances waiting time and turnaround time using a weighted optimization approach.
🏆 Reinforcement Learning (Q-learning) Optimization
AI learns optimal scheduling strategies based on reward-based learning.
State representation: Remaining processes & execution time.
Action space: Selecting the next process to execute.
Reward function: Minimizes waiting time dynamically by learning the best order.
🔹 Performance Metrics & Analysis
Average Waiting Time: Measures process idle duration before execution.
Turnaround Time: Measures total time from arrival to completion.
CPU Utilization: Evaluates how efficiently CPU resources are utilized.
Throughput: Calculates the number of completed processes per unit time.
Gantt Charts: Visual representations of scheduling execution sequences.
📂 Project Structure
plaintext


cpu_scheduler_project/
├── README.md              # Project documentation and usage guide
├── requirements.txt       # List of required Python dependencies
├── Dockerfile             # Docker container configuration
├── .github/workflows/ci.yml # GitHub Actions workflow for CI/CD
├── scheduler.py           # Classical CPU scheduling algorithms (FCFS, RR, Priority, SJF, Preemptive)
├── metrics.py             # Performance metric calculations (waiting time, turnaround time, CPU usage)
├── demo_algorithms.py     # Scheduling demonstrations + Gantt chart visualization
├── optimizer.py           # AI-based Genetic Algorithm (GA) optimization for scheduling
├── advanced_ai.py         # Q-learning based Reinforcement Learning for scheduling optimization
├── main.py                # Runs all demos, AI optimizations, and logs results
└── results/               # Stores CSV files with performance data


⚡ Installation
1️⃣ Clone the Repository:


git clone https://github.com/Taylanozveren/CPU-Project-Improved-AI-Models.git
cd CPU-Project-Improved-AI-Models
2️⃣ Set Up a Virtual Environment (Recommended):

Windows:


python -m venv venv
venv\Scripts\activate


Linux/Mac:


python3 -m venv venv
source venv/bin/activate

3️⃣ Upgrade pip, setuptools, and weel:
venv\Scripts\python.exe -m pip install --upgrade pip setuptools wheel

4️⃣ Install Required Dependencies:
pip install -r requirements.txt


🛠 Usage
Run the main script to execute scheduling algorithms, AI-based optimizations, and generate reports.
python main.py

📊 Expected Outputs:

Terminal output displaying scheduling orders, performance metrics, and comparisons.
Gantt Charts for each algorithm.
CSV File Output: Results saved in results/final_results.csv.


🐳 Docker Integration
To run the project inside a Docker container for consistent execution:

1️⃣ Build the Docker Image:
docker build -t cpu_scheduler:latest .

2️⃣ Run the Container:
docker run --rm cpu_scheduler:latest

🔄 Continuous Integration (CI)
A GitHub Actions workflow (.github/workflows/ci.yml) automates dependency installation & testing on each code push.
Ensures code stability by verifying scheduling algorithms and AI optimization models.


🚀 Future Enhancements
✅ Advanced Reinforcement Learning: Improve Q-learning models with deeper state-action space.
✅ Real-Time & Multi-Core Scheduling: Extend scheduling strategies to support multi-core CPU environments.
✅ Hybrid AI Models: Combine Genetic Algorithms & RL for intelligent process scheduling.
✅ Cloud Integration: Deploy as a cloud-based API for dynamic scheduling optimization.

This project bridges OS fundamentals with AI-driven optimization, providing a robust framework for intelligent CPU scheduling strategies. 🎯

---

### 🔹 **Key Improvements in this README**  
✅ **Clearer Structure:** Organized sections with concise yet detailed explanations.  
✅ **Stronger AI & Data Science Explanation:** Highlights how Genetic Algorithms and Q-learning optimize scheduling.  
✅ **Better Readability:** Clean formatting, emojis for visual clarity, and direct command-line instructions.  
✅ **Professional & Technical Clarity:** Ideal for LinkedIn, GitHub, and portfolio presentations.  






