import tkinter as tk

# Import your algorithms
from fcfs import fcfs
from sjf import sjf
from round_robin import round_robin
from priority import priority_scheduling
from utils import calculate_metrics
from tkinter import ttk

# ---------------- WINDOW ----------------
root = tk.Tk()
root.title("CPU Scheduling Analysis Tool")
root.geometry("900x700")

# ---------------- INPUT STORAGE ----------------
entries = []

# ---------------- FUNCTIONS ----------------

def create_inputs():
    global entries
    entries = []

    # clear old inputs
    for widget in input_frame.winfo_children():
        widget.destroy()

    n = int(n_entry.get())

    for i in range(n):
        row = []

        tk.Label(input_frame, text=f"P{i+1} AT").grid(row=i, column=0)
        at = tk.Entry(input_frame, width=5)
        at.grid(row=i, column=1)

        tk.Label(input_frame, text="BT").grid(row=i, column=2)
        bt = tk.Entry(input_frame, width=5)
        bt.grid(row=i, column=3)

        tk.Label(input_frame, text="PR").grid(row=i, column=4)
        pr = tk.Entry(input_frame, width=5)
        pr.grid(row=i, column=5)

        row.extend([at, bt, pr])
        entries.append(row)


def get_input_data():
    processes = []

    for i, row in enumerate(entries):
        at = int(row[0].get())
        bt = int(row[1].get())
        pr = int(row[2].get())

        processes.append({
            "id": f"P{i+1}",
            "at": at,
            "bt": bt,
            "priority": pr
        })

    return processes


def display_output(processes):
    # Clear old data
    for row in tree.get_children():
        tree.delete(row)

    # Insert new data
    for p in processes:
        tree.insert("", tk.END, values=(
            p["id"],
            p["at"],
            p["bt"],
            p["ct"],
            p["tat"],
            p["wt"]
        ))


# ---------------- ALGORITHM FUNCTIONS ----------------

def run_fcfs():
    processes = get_input_data()
    result = fcfs(processes)
    result = calculate_metrics(result)
    display_output(result)


def run_sjf():
    processes = get_input_data()
    result = sjf(processes)
    result = calculate_metrics(result)
    display_output(result)


def run_rr():
    processes = get_input_data()
    q = int(quantum_entry.get())

    result, gantt = round_robin(processes, q)
    result = calculate_metrics(result)

    display_output(result)

    output.insert(tk.END, "\nGantt Chart:\n")
    for g in gantt:
        output.insert(tk.END, f"{g} ")
    output.insert(tk.END, "\n")


def run_priority():
    processes = get_input_data()
    result = priority_scheduling(processes)
    result = calculate_metrics(result)
    display_output(result)


# ---------------- UI ----------------

tk.Label(root, text="CPU Scheduling Tool", font=("Arial", 18)).pack(pady=10)

# Number of processes
tk.Label(root, text="Number of Processes").pack()
n_entry = tk.Entry(root)
n_entry.pack()

tk.Button(root, text="Create Inputs", command=create_inputs).pack(pady=10)

# Input area
input_frame = tk.Frame(root)
input_frame.pack()

# Quantum input (for RR)
tk.Label(root, text="Time Quantum (RR)").pack()
quantum_entry = tk.Entry(root)
quantum_entry.pack()

# Buttons
tk.Button(root, text="Run FCFS", command=run_fcfs).pack(pady=5)
tk.Button(root, text="Run SJF", command=run_sjf).pack(pady=5)
tk.Button(root, text="Run Round Robin", command=run_rr).pack(pady=5)
tk.Button(root, text="Run Priority", command=run_priority).pack(pady=5)

# Output box
columns = ("ID", "AT", "BT", "CT", "TAT", "WT")

tree = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=80)

tree.pack(pady=10)

# ---------------- RUN ----------------
root.mainloop()