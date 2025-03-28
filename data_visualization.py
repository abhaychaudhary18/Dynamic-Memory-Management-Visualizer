import matplotlib.pyplot as plt

def visualize_memory_allocation(memory_allocation):
    frames = range(len(memory_allocation))
    pages = memory_allocation

    # Create a color list: blue for allocated, gray for free
    colors = ['skyblue' if page else 'lightgray' for page in pages]

    plt.bar(frames, [1] * len(frames), color=colors)  # Use height=1 for uniform bars
    plt.xlabel('Memory Frames')
    plt.ylabel('Allocation Status')
    plt.title('Memory Allocation')
    plt.xticks(frames)
    
    # Add labels for each bar
    for i, page in enumerate(pages):
        plt.text(i, 0.5, page if page else "Free", ha='center', va='bottom', rotation=90)
    
    # Add legend
    plt.legend(["Allocated", "Free"], loc="upper right")
    plt.show()

def visualize_page_faults(page_faults_over_time):
    time_steps = range(len(page_faults_over_time))
    faults = page_faults_over_time

    plt.plot(time_steps, faults, marker='o', color='red', label="Page Faults")
    plt.xlabel('Time Steps')
    plt.ylabel('Page Faults')
    plt.title('Page Faults Over Time')
    plt.grid(True)
    
    # Annotate each page fault
    for i, fault in enumerate(faults):
        if fault > (faults[i-1] if i > 0 else 0):
            plt.annotate(f'Fault {fault}', (i, fault), textcoords="offset points", xytext=(0,10), ha='center')
    
    plt.legend()
    plt.show()

def visualize_gantt_chart(allocation_timeline):
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Create a dictionary to map pages to their allocation times
    page_allocation = {}
    for time, page, memory in allocation_timeline:
        if page not in page_allocation:
            page_allocation[page] = []
        page_allocation[page].append((time, memory.index(page) if page in memory else None))
    
    # Plot each page's allocation
    for i, (page, allocations) in enumerate(page_allocation.items()):
        for time, frame in allocations:
            if frame is not None:
                ax.broken_barh([(time, 1)], (frame, 0.8), facecolors=('skyblue'))
    
    # Set labels and title
    ax.set_xlabel('Time Steps')
    ax.set_ylabel('Memory Frames')
    ax.set_title('Gantt Chart: Page Allocation Over Time')
    ax.set_yticks(range(len(allocation_timeline[0][2])))  # Number of frames
    ax.set_yticklabels([f"Frame {i}" for i in range(len(allocation_timeline[0][2]))])
    ax.grid(True)
    
    plt.show()
