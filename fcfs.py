def fcfs(processes):
    # Sort by arrival time
    processes = sorted(processes, key=lambda x: x["at"])

    time = 0

    for p in processes:
        # If CPU is idle, jump to arrival time
        if time < p["at"]:
            time = p["at"]

        # Execute process
        time += p["bt"]

        # Set Completion Time
        p["ct"] = time

    return processes