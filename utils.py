def calculate_metrics(processes):
    for p in processes:
        p["tat"] = p["ct"] - p["at"]
        p["wt"] = p["tat"] - p["bt"]
    return processes
def print_table(processes):
    print("\nProcess AT BT CT TAT WT")
    for p in processes:
        print(f"{p['id']}     {p['at']}  {p['bt']}  {p['ct']}  {p['tat']}   {p['wt']}")