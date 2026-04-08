def priority_scheduling(processes):
    processes = processes[:]
    completed = []
    time = 0

    while processes:
        # get available processes
        available = [p for p in processes if p["at"] <= time]

        if not available:
            time = min(p["at"] for p in processes)
            continue

        # select highest priority (lowest number)
        p = min(available, key=lambda x: x["priority"])

        processes.remove(p)

        time += p["bt"]
        p["ct"] = time

        completed.append(p)

    return completed