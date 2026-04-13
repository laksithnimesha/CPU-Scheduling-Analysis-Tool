import tkinter as tk
import matplotlib.pyplot as plt
from tkinter import ttk

# Import algorithms
from fcfs import fcfs
from sjf import sjf
from round_robin import round_robin
from priority import priority_scheduling
from utils import calculate_metrics
from compare import compare


# ---------------- WINDOW ----------------
root = tk.Tk()
root.title("CPU Scheduling Analysis Tool")
root.geometry("1000x700")

# ---------------- FRAMES ----------------
top_frame = tk.Frame(root)
top_frame.pack(pady=10)

middle_frame = tk.Frame(root)
middle_frame.pack(pady=10)

left_frame = tk.Frame(middle_frame)
left_frame.pack(side="left", padx=30)

right_frame = tk.Frame(middle_frame)
right_frame.pack(side="right", padx=30)

bottom_frame = tk.Frame(root)
bottom_frame.pack(pady=10)

# ---------------- TITLE ----------------
tk.Label(top_frame, text="CPU Scheduling Analysis Tool", font=("Arial", 18)).pack()

# ---------------- INPUT ----------------
entries = []

tk.Label(left_frame, text="Number of Processes").pack()
n_entry = tk.Entry(left_frame)
n_entry.pack()

def create_inputs():
    global entries
    entries = []

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

tk.Button(left_frame, text="Create Inputs", command=create_inputs).pack(pady=10)

input_frame = tk.Frame(left_frame)
input_frame.pack()

# ---------------- QUANTUM ----------------
tk.Label(left_frame, text="Time Quantum (RR)").pack()
quantum_entry = tk.Entry(left_frame)
quantum_entry.pack()

# ---------------- TABLE ----------------
columns = ("ID", "AT", "BT", "CT", "TAT", "WT")

tree = ttk.Treeview(bottom_frame, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=80)

tree.pack()

# ---------------- GANTT ----------------
gantt_text = tk.Text(root, height=4, width=100)
gantt_text.pack(pady=10)

# ---------------- FUNCTIONS ----------------

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
    for row in tree.get_children():
        tree.delete(row)

    for p in processes:
        tree.insert("", tk.END, values=(
            p["id"],
            p["at"],
            p["bt"],
            p["ct"],
            p["tat"],
            p["wt"]
        ))


def display_gantt(gantt):
    gantt_text.delete(1.0, tk.END)

    for g in gantt:
        gantt_text.insert(tk.END, f"| {g[0]} ")

    gantt_text.insert(tk.END, "|\n0 ")

    for g in gantt:
        gantt_text.insert(tk.END, f"  {g[2]}")


# ---------------- ALGORITHMS ----------------

def run_fcfs():
    processes = get_input_data()
    result = fcfs(processes)
    result = calculate_metrics(result)

    display_output(result)
    gantt_text.delete(1.0, tk.END)


def run_sjf():
    processes = get_input_data()
    result = sjf(processes)
    result = calculate_metrics(result)

    display_output(result)
    gantt_text.delete(1.0, tk.END)


def run_rr():
    processes = get_input_data()
    q = int(quantum_entry.get())

    result, gantt = round_robin(processes, q)
    result = calculate_metrics(result)

    display_output(result)
    display_gantt(gantt)


def run_priority():
    processes = get_input_data()
    result = priority_scheduling(processes)
    result = calculate_metrics(result)

    display_output(result)
    gantt_text.delete(1.0, tk.END)


def run_compare():
    processes = get_input_data()

    # Clear table
    for row in tree.get_children():
        tree.delete(row)

    # Clear gantt
    gantt_text.delete(1.0, tk.END)

    # Run all algorithms
    from fcfs import fcfs
    from sjf import sjf
    from priority import priority_scheduling
    from round_robin import round_robin

    results = {}

    # FCFS
    temp = [p.copy() for p in processes]
    res = calculate_metrics(fcfs(temp))
    results["FCFS"] = (
        sum(p["wt"] for p in res)/len(res),
        sum(p["tat"] for p in res)/len(res)
    )

    # SJF
    temp = [p.copy() for p in processes]
    res = calculate_metrics(sjf(temp))
    results["SJF"] = (
        sum(p["wt"] for p in res)/len(res),
        sum(p["tat"] for p in res)/len(res)
    )

    # Priority
    temp = [p.copy() for p in processes]
    res = calculate_metrics(priority_scheduling(temp))
    results["Priority"] = (
        sum(p["wt"] for p in res)/len(res),
        sum(p["tat"] for p in res)/len(res)
    )

    # Round Robin
    q = int(quantum_entry.get())
    temp = [p.copy() for p in processes]
    res, _ = round_robin(temp, q)
    res = calculate_metrics(res)
    results["RR"] = (
        sum(p["wt"] for p in res)/len(res),
        sum(p["tat"] for p in res)/len(res)
    )

    # Display in text area
    gantt_text.insert(tk.END, "Algorithm Comparison:\n")
    gantt_text.insert(tk.END, "Algo     Avg WT   Avg TAT\n")

    for k, v in results.items():
        gantt_text.insert(tk.END, f"{k:8} {round(v[0],2):7} {round(v[1],2):9}\n")

    show_graph(results)    


def show_graph(results):
    algorithms = list(results.keys())
    avg_wt = [v[0] for v in results.values()]
    avg_tat = [v[1] for v in results.values()]

    x = range(len(algorithms))

    plt.figure()

    # Waiting Time bars
    plt.bar(x, avg_wt)

    # Labels
    plt.xticks(x, algorithms)
    plt.xlabel("Algorithms")
    plt.ylabel("Average Time")
    plt.title("CPU Scheduling Comparison")

    plt.show()        

# ---------------- BUTTONS ----------------

tk.Button(right_frame, text="Run FCFS", width=20, command=run_fcfs).pack(pady=5)
tk.Button(right_frame, text="Run SJF", width=20, command=run_sjf).pack(pady=5)
tk.Button(right_frame, text="Run Round Robin", width=20, command=run_rr).pack(pady=5)
tk.Button(right_frame, text="Run Priority", width=20, command=run_priority).pack(pady=5)
tk.Button(right_frame, text="Compare All", width=20, command=run_compare).pack(pady=5)

# ---------------- RUN ----------------
root.mainloop()