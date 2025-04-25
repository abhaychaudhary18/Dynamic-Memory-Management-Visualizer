# Dynamic Memory Management Visualizer

An educational Operating System project that simulates **page replacement algorithms** to help visualize memory management strategies in action. Designed with a GUI for user interaction and insights.

## 🧠 Overview

Memory management is a core component of modern operating systems. This visualizer simulates two key **page replacement algorithms**:

- **FIFO (First-In-First-Out)**
- **LRU (Least Recently Used)**

It provides a hands-on tool to observe how pages are replaced and how page faults occur during memory operations.

## 🎯 Objectives

- Simulate paging-based memory management.
- Provide real-time visual feedback for:
  - Page faults over time.
  - Memory allocation and replacement.
  - Gantt chart of frame occupancy.

## 🛠️ Tech Stack

- **Language:** Python
- **GUI:** Tkinter
- **Visualization:** Matplotlib
- **Algorithms:** FIFO & LRU

## 🏗️ System Architecture

- **Input Module:** Accepts process details, memory configuration, and algorithm choice.
- **Simulation Engine:** Manages memory frames, page faults, and replacement logic.
- **GUI Layer:** Handles user input and displays visual results.
- **Visualization Module:** Plots memory allocation, faults, and Gantt charts.

## 🖥️ GUI Features

1. **Configuration Panel** – Set memory size and page size.
2. **Algorithm Selector** – Choose between FIFO or LRU.
3. **Visualization Output** – Graphs and Gantt charts for analysis.

## 📈 Sample Visualizations

- **Memory Allocation View** – Displays status of each memory frame.
- **Page Fault Graph** – Tracks cumulative faults over time.
- **Gantt Chart** – Shows page/frame occupancy over the simulation timeline.

## 📌 Conclusion

This project aims to make **dynamic memory management** more intuitive through visualization. It highlights the performance differences of algorithms and supports further extension with more strategies.

---

### 👩‍💻 Developed by:

> Priyam Tiwari & Team  
> Computer Science Department

---

### 📂 License

This project is licensed under the [MIT License](LICENSE).

