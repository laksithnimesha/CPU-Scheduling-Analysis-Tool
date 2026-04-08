from fcfs import fcfs
from sjf import sjf
from round_robin import round_robin
from utils import calculate_metrics, print_table, gantt_chart, averages


def get_processes():
    n = int(input("Enter number of processes: "))
    processes = []

    for i in range(n):
        print(f"\nProcess P{i+1}")
        at = int(input("Arrival Time: "))
        bt = int(input("Burst Time: "))

        processes.append({
            "id": f"P{i+1}",
            "at": at,
            "bt": bt
        })

    return processes


# Main Execution
processes = get_processes()

print("\n1. FCFS")
print("2. SJF")
print("3. Round Robin")

choice = int(input("Choose algorithm: "))

if choice == 1:
    result = fcfs(processes)
    gantt = None

elif choice == 2:
    result = sjf(processes)
    gantt = None

elif choice == 3:
    q = int(input("Enter time quantum: "))
    result, gantt = round_robin(processes, q)

else:
    print("Invalid choice!")
    exit()

# Metrics
result = calculate_metrics(result)

print("\nScheduling Result:")
print_table(result)

# 🔥 Gantt handling
print("\nGantt Chart:")

if gantt:   # Round Robin
    print("|", end="")
    for g in gantt:
        print(f" {g[0]} |", end="")

    print("\n0", end="")
    for g in gantt:
        print(f"   {g[2]}", end="")
    print()

else:   # FCFS & SJF
    gantt_chart(result)

# Averages
averages(result)