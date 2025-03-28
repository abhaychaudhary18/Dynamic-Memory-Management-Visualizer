from collections import deque

class MemoryManagementSimulator:
    def __init__(self, memory_size, page_size):
        self.memory_size = memory_size
        self.page_size = page_size
        self.num_frames = memory_size // page_size
        self.memory = [None] * self.num_frames  # Represents memory frames
        self.page_table = {}  # Maps pages to frames
        self.page_faults = 0
        self.page_faults_over_time = []  # Track page faults over time
        self.allocation_timeline = []  # Track allocation timeline

    def fifo_page_replacement(self, page):
        if page in self.page_table:
            return  # Page is already in memory
        
        if None in self.memory:
            # If there's an empty frame, use it
            frame_index = self.memory.index(None)
        else:
            # Replace the oldest page (FIFO)
            frame_index = self.fifo_queue.popleft()
        
        # Update memory and page table
        self.memory[frame_index] = page
        self.page_table[page] = frame_index
        self.fifo_queue.append(frame_index)
        self.page_faults += 1

    def lru_page_replacement(self, page):
        if page in self.page_table:
            # Update the page's access time (LRU)
            self.access_times[page] = self.current_time
            return  # Page is already in memory
        
        if None in self.memory:
            # If there's an empty frame, use it
            frame_index = self.memory.index(None)
        else:
            # Replace the least recently used page (LRU)
            lru_page = min(self.access_times.keys(), key=lambda k: self.access_times[k])
            frame_index = self.page_table[lru_page]
            del self.page_table[lru_page]
        
        # Update memory, page table, and access times
        self.memory[frame_index] = page
        self.page_table[page] = frame_index
        self.access_times[page] = self.current_time
        self.page_faults += 1

    def simulate(self, processes, algorithm="FIFO"):
        self.page_faults = 0
        self.fifo_queue = deque()  # For FIFO
        self.access_times = {}  # For LRU
        self.current_time = 0
        self.page_faults_over_time = []  # Track page faults over time
        self.allocation_timeline = []  # Track allocation timeline

        for process in processes:
            pages = self._get_pages_for_process(process)
            for page in pages:
                if algorithm == "FIFO":
                    self.fifo_page_replacement(page)
                elif algorithm == "LRU":
                    self.lru_page_replacement(page)
                self.current_time += 1
                self.page_faults_over_time.append(self.page_faults)
                self.allocation_timeline.append((self.current_time, page, self.memory.copy()))

        return {
            "page_faults": self.page_faults,
            "memory_allocation": self.memory,
            "page_table": self.page_table,
            "page_faults_over_time": self.page_faults_over_time,
            "allocation_timeline": self.allocation_timeline
        }

    def _get_pages_for_process(self, process):
        # Divide the process's memory requirements into pages
        memory_required = int(process["Burst Time"])
        num_pages = (memory_required + self.page_size - 1) // self.page_size
        return [f"{process['Process ID']}_Page{i}" for i in range(num_pages)]
