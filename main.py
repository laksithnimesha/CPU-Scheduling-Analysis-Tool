from fcfs import fcfs
from sjf import sjf
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

choice = int(input("Choose algorithm: "))

if choice == 1:
    result = fcfs(processes)

elif choice == 2:
    result = sjf(processes)

else:
    print("Invalid choice!")
    exit()

# Calculate metrics
result = calculate_metrics(result)

# Display results
print("\nScheduling Result:")
print_table(result)

# Gantt chart
gantt_chart(result)

# Averages
averages(result)