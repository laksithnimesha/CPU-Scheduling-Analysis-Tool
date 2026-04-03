from fcfs import fcfs
from utils import calculate_metrics
from utils import calculate_metrics, print_table
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


processes = get_processes()

result = fcfs(processes)

result = calculate_metrics(result)

print("\nAfter FCFS Scheduling:")
for p in result:
    print(p)
    print_table(result)