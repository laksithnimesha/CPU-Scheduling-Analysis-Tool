def round_robin(processes, quantum):
    processes = processes[:]  
    time = 0
    queue = []
    completed = []
    gantt = []   # 🔥 NEW

    processes.sort(key=lambda x: x["at"])

    for p in processes:
        p["remaining"] = p["bt"]

    i = 0
    n = len(processes)

    while len(completed) < n:

        while i < n and processes[i]["at"] <= time:
            queue.append(processes[i])
            i += 1

        if not queue:
            time += 1
            continue

        current = queue.pop(0)

        exec_time = min(quantum, current["remaining"])

        gantt.append((current["id"], time, time + exec_time))  # 🔥 TRACK

        time += exec_time
        current["remaining"] -= exec_time

        while i < n and processes[i]["at"] <= time:
            queue.append(processes[i])
            i += 1

        if current["remaining"] > 0:
            queue.append(current)
        else:
            current["ct"] = time
            completed.append(current)

    return completed, gantt   # 🔥 RETURN BOTH