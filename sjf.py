def sjf(processes):
    time = 0
    completed = []

    processes = processes[:]  # copy list

    while processes:
        # Get available processes
        available = [p for p in processes if p["at"] <= time]

        if not available:
            time += 1
            continue

        # Select shortest job
        p = min(available, key=lambda x: x["bt"])

        processes.remove(p)

        time += p["bt"]
        p["ct"] = time

        completed.append(p)

    return completed