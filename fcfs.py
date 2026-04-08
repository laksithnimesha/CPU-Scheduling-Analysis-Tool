def fcfs(processes):
    # Sort by arrival time
    processes = sorted(processes, key=lambda x: x["at"])

    time = 0

    for p in processes:
        # If CPU is idle
        if time < p["at"]:
            time = p["at"]

        # Execute process
        time += p["bt"]

        # Completion time
        p["ct"] = time

    return processes