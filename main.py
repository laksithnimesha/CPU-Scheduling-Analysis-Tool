from fcfs import fcfs
from sjf import sjf
from round_robin import round_robin
from priority import priority_scheduling
from compare import compare
from utils import calculate_metrics, print_table, gantt_chart, averages


def get_processes():
    n = int(input("Enter number of processes: "))
    processes = []

    for i in range(n):
        print(f"\nProcess P{i+1}")
        at = int(input("Arrival Time: "))
        bt = int(input("Burst Time: "))
        pr = int(input("Priority: "))

        processes.append({
            "id": f"P{i+1}",
            "at": at,
            "bt": bt,
            "priority": pr
        })

    return processes


# Main Execution
processes = get_processes()

print("\n1. FCFS")
print("2. SJF")
print("3. Round Robin")
print("4. Priority")
print("5. Compare All")
print("6. Run All Algorithms")

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

elif choice == 4:
    result = priority_scheduling(processes)
    gantt = None    

elif choice == 5:
    compare(processes)
    exit()    

elif choice == 6:
    print("\n========== FCFS ==========")
    temp = [p.copy() for p in processes]
    res = fcfs(temp)
    res = calculate_metrics(res)
    print_table(res)
    gantt_chart(res)
    averages(res)

    print("\n========== SJF ==========")
    temp = [p.copy() for p in processes]
    res = sjf(temp)
    res = calculate_metrics(res)
    print_table(res)
    gantt_chart(res)
    averages(res)

    print("\n========== Round Robin ==========")
    q = int(input("Enter time quantum: "))
    temp = [p.copy() for p in processes]
    res, gantt = round_robin(temp, q)
    res = calculate_metrics(res)
    print_table(res)

    print("\nGantt Chart:")
    print("|", end="")
    for g in gantt:
        print(f" {g[0]} |", end="")
    print("\n0", end="")
    for g in gantt:
        print(f"   {g[2]}", end="")
    print()
    averages(res)

    print("\n========== Priority ==========")
    temp = [p.copy() for p in processes]
    res = priority_scheduling(temp)
    res = calculate_metrics(res)
    print_table(res)
    gantt_chart(res)
    averages(res)

    print("\n========== FINAL COMPARISON ==========")
    compare(processes)

    exit()    

else:
    print("Invalid choice!")
    exit()

# Metrics
result = calculate_metrics(result)

print("\nScheduling Result:")
print_table(result)

# Gantt handling
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