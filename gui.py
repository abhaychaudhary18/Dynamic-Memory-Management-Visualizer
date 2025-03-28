import tkinter as tk
from tkinter import ttk
from memory_management_simulator import MemoryManagementSimulator
from data_visualization import visualize_memory_allocation, visualize_page_faults, visualize_gantt_chart

# Create the main window
root = tk.Tk()
root.title("Dynamic Memory Management Visualizer")
root.geometry("600x500")

# Function to handle the "Simulate" button click
def simulate():
    try:
        # Get inputs from the GUI
        memory_size = int(memory_size_entry.get())
        page_size = int(page_size_entry.get())
        algorithm = algorithm_combobox.get()
        visualization = visualization_combobox.get()
        
        # Validate inputs
        if memory_size <= 0 or page_size <= 0:
            raise ValueError("Memory size and page size must be positive integers.")
        
        # Collect process details
        processes = []
        for i, (arrival_time, burst_time) in enumerate(process_entries):
            try:
                processes.append({
                    "Process ID": f"P{i+1}",
                    "Arrival Time": int(arrival_time.get()),
                    "Burst Time": int(burst_time.get())
                })
            except ValueError:
                raise ValueError(f"Invalid input for Process P{i+1}. Arrival Time and Burst Time must be integers.")
        
        # Initialize the simulator
        simulator = MemoryManagementSimulator(memory_size, page_size)
        
        # Run the simulation
        results = simulator.simulate(processes, algorithm)
        
        # Display the results
        result_label.config(text=f"Page Faults: {results['page_faults']}")
        
        # Display memory allocation
        memory_allocation_text = "Memory Allocation:\n"
        for i, page in enumerate(results["memory_allocation"]):
            memory_allocation_text += f"Frame {i}: {page}\n"
        memory_allocation_label.config(text=memory_allocation_text)
        
        # Display page table
        page_table_text = "Page Table:\n"
        for page, frame in results["page_table"].items():
            page_table_text += f"{page} -> Frame {frame}\n"
        page_table_label.config(text=page_table_text)
        
        # Show selected visualization
        if visualization == "Memory Allocation":
            visualize_memory_allocation(results["memory_allocation"])
        elif visualization == "Page Faults":
            visualize_page_faults(results["page_faults_over_time"])
        elif visualization == "Gantt Chart":
            visualize_gantt_chart(results["allocation_timeline"])
    
    except ValueError as e:
        # Show error message in the GUI
        result_label.config(text=f"Error: {str(e)}", fg="red")

# Function to reset all inputs and results
def reset():
    memory_size_entry.delete(0, tk.END)
    page_size_entry.delete(0, tk.END)
    algorithm_combobox.current(0)
    visualization_combobox.current(0)
    for arrival_time, burst_time in process_entries:
        arrival_time.delete(0, tk.END)
        burst_time.delete(0, tk.END)
    result_label.config(text="Page Faults: ")
    memory_allocation_label.config(text="Memory Allocation:")
    page_table_label.config(text="Page Table:")

# Memory Size Input
memory_size_label = tk.Label(root, text="Memory Size:")
memory_size_label.grid(row=0, column=0, padx=10, pady=10)
memory_size_entry = tk.Entry(root)
memory_size_entry.grid(row=0, column=1, padx=10, pady=10)

# Page Size Input
page_size_label = tk.Label(root, text="Page Size:")
page_size_label.grid(row=1, column=0, padx=10, pady=10)
page_size_entry = tk.Entry(root)
page_size_entry.grid(row=1, column=1, padx=10, pady=10)

# Replacement Algorithm Selection
algorithm_label = tk.Label(root, text="Replacement Algorithm:")
algorithm_label.grid(row=2, column=0, padx=10, pady=10)
algorithm_combobox = ttk.Combobox(root, values=["FIFO", "LRU"])
algorithm_combobox.grid(row=2, column=1, padx=10, pady=10)
algorithm_combobox.current(0)  # Set default to FIFO

# Process Input Table
process_label = tk.Label(root, text="Process Details:")
process_label.grid(row=3, column=0, padx=10, pady=10)
tk.Label(root, text="Process ID").grid(row=4, column=0, padx=5, pady=5)
tk.Label(root, text="Arrival Time").grid(row=4, column=1, padx=5, pady=5)
tk.Label(root, text="Burst Time").grid(row=4, column=2, padx=5, pady=5)

process_entries = []
for i in range(3):  # Allow 3 processes for now
    process_id = tk.Label(root, text=f"P{i+1}")
    process_id.grid(row=5+i, column=0, padx=5, pady=5)
    
    arrival_time = tk.Entry(root, width=10)
    arrival_time.grid(row=5+i, column=1, padx=5, pady=5)
    
    burst_time = tk.Entry(root, width=10)
    burst_time.grid(row=5+i, column=2, padx=5, pady=5)
    
    process_entries.append((arrival_time, burst_time))

# Simulate Button
simulate_button = tk.Button(root, text="Simulate", command=simulate)
simulate_button.grid(row=8, column=0, columnspan=2, pady=20)

# Reset Button
reset_button = tk.Button(root, text="Reset", command=reset)
reset_button.grid(row=8, column=2, padx=10, pady=20)

# Visualization Selection
visualization_label = tk.Label(root, text="Select Visualization:")
visualization_label.grid(row=9, column=0, padx=10, pady=10)
visualization_combobox = ttk.Combobox(root, values=["Memory Allocation", "Page Faults", "Gantt Chart"])
visualization_combobox.grid(row=9, column=1, padx=10, pady=10)
visualization_combobox.current(0)  # Set default to Memory Allocation

# Result Label
result_label = tk.Label(root, text="Page Faults: ")
result_label.grid(row=10, column=0, columnspan=3, pady=10)

# Memory Allocation Label
memory_allocation_label = tk.Label(root, text="Memory Allocation:")
memory_allocation_label.grid(row=11, column=0, columnspan=3, pady=10)

# Page Table Label
page_table_label = tk.Label(root, text="Page Table:")
page_table_label.grid(row=12, column=0, columnspan=3, pady=10)

# Run the application
root.mainloop()
