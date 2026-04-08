def calculate_metrics(processes):
    for p in processes:
        p["tat"] = p["ct"] - p["at"]   # Turnaround Time
        p["wt"] = p["tat"] - p["bt"]   # Waiting Time
    return processes


def print_table(processes):
    print("\nProcess AT BT CT TAT WT")
    for p in processes:
        print(f"{p['id']}     {p['at']}  {p['bt']}  {p['ct']}  {p['tat']}   {p['wt']}")


def gantt_chart(processes):
    print("\nGantt Chart:")

    # Process order
    print("|", end="")
    for p in processes:
        print(f" {p['id']} |", end="")
    print()

    # Timeline
    print("0", end="")
    for p in processes:
        print(f"   {p['ct']}", end="")
    print()


def averages(processes):
    total_wt = sum(p["wt"] for p in processes)
    total_tat = sum(p["tat"] for p in processes)

    avg_wt = total_wt / len(processes)
    avg_tat = total_tat / len(processes)

    print("\nAverage Waiting Time:", round(avg_wt, 2))
    print("Average Turnaround Time:", round(avg_tat, 2))