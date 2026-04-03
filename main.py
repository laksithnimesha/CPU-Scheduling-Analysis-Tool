from fcfs import fcfs
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

# Run FCFS
result = fcfs(processes)

# Calculate metrics
result = calculate_metrics(result)

# Display results
print("\nAfter FCFS Scheduling:")
print_table(result)

# Show Gantt Chart
gantt_chart(result)

# Show averages
averages(result)