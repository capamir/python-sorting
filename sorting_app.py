import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import time

def plot_sorting_algorithms():
    # Given data
    list_length = [1000, 5000, 10000, 50000, 100000, 200000, 300000]
    bubble_sort = [0.0, 0.145, 0.6, 14.05, 56.9, 229.44, 513.34]
    insertion_sort = [0.0, 0.045, 0.18, 4.25, 17.62, 69.12, 154.22]
    quick_sort = [0.0, 0.0, 0.0, 0.01, 0.02, 0.05, 0.065]

    # Create a line plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(list_length, bubble_sort, label='Bubble Sort', marker='o')
    ax.plot(list_length, insertion_sort, label='Insertion Sort', marker='s')
    ax.plot(list_length, quick_sort, label='Quicksort', marker='^')

    # Add labels and title
    ax.set_xlabel('List Length')
    ax.set_ylabel('Runtime (seconds)')
    ax.set_title('Sorting Algorithms Runtime vs. List Length')
    ax.grid(True)
    ax.legend()

    # Displaying plot
    canvas = FigureCanvasTkAgg(fig, master=header_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

def bubble_sort(arr):
    steps = 0
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            steps += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return steps

def insertion_sort(arr):
    steps = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        steps += 1
        while j >= 0 and key < arr[j]:
            steps += 1
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return steps

def get_input():
    user_input = input_entry.get()
    input_list = [int(x.strip()) for x in user_input.split(',')]
    
    # Sorting using bubble sort
    bubble_start_time = time.time()
    bubble_steps = bubble_sort(input_list.copy())
    bubble_end_time = time.time()
    bubble_time_taken = bubble_end_time - bubble_start_time

    # Sorting using insertion sort
    insertion_start_time = time.time()
    insertion_steps = insertion_sort(input_list.copy())
    insertion_end_time = time.time()
    insertion_time_taken = insertion_end_time - insertion_start_time

    # Display results
    result_label.config(text=f"Bubble Sort:\nTime taken: {bubble_time_taken:.6f} seconds\nSteps: {bubble_steps}\n\n"
                              f"Insertion Sort:\nTime taken: {insertion_time_taken:.6f} seconds\nSteps: {insertion_steps}")

# Creating main window
root = tk.Tk()
root.title("Sorting Algorithms Performance")

# Creating header frame
header_frame = tk.Frame(root)
header_frame.pack()

# Plotting sorting algorithms graph
plot_sorting_algorithms()

# Creating input frame
input_frame = tk.Frame(root)
input_frame.pack()

# Creating input label and entry
input_label = ttk.Label(input_frame, text="Enter comma-separated integers:", font=('Helvetica', 18))
input_label.pack(side=tk.LEFT)
input_entry = ttk.Entry(input_frame, width=40, font=('Helvetica', 16))
input_entry.pack(side=tk.LEFT)

# Creating button to trigger sorting
input_button = ttk.Button(root, text="Sort", command=get_input, width=30)
input_button.pack()

# Creating result label
result_label = ttk.Label(root, text="", font=('Helvetica', 18))
result_label.pack()

# Running the Tkinter event loop
root.mainloop()
