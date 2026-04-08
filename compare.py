from fcfs import fcfs
from sjf import sjf
from priority import priority_scheduling
from round_robin import round_robin
from utils import calculate_metrics

def compare(processes):
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

    # Round Robin (fixed quantum = 2 for comparison)
    temp = [p.copy() for p in processes]
    res, _ = round_robin(temp, 2)
    res = calculate_metrics(res)
    results["RR(q=2)"] = (
        sum(p["wt"] for p in res)/len(res),
        sum(p["tat"] for p in res)/len(res)
    )

    print("\nAlgorithm Comparison:")
    print("Algorithm   Avg WT   Avg TAT")

    for k, v in results.items():
        print(f"{k:10} {round(v[0],2):7} {round(v[1],2):9}")