import multiprocessing
import time

def stress_cpu(load_percent: float, interval: float = 0.1):
    """
    Keep CPU at approximately `load_percent`% usage.
    Uses busy loop + sleep duty cycling.
    """
    busy_time = interval * load_percent
    idle_time = interval - busy_time

    while True:
        start = time.time()
        # Busy loop for busy_time seconds
        while (time.time() - start) < busy_time:
            pass
        # Then sleep for idle_time seconds
        if idle_time > 0:
            time.sleep(idle_time)

if __name__ == "__main__":
    num_cores = multiprocessing.cpu_count()
    print(f"Detected {num_cores} cores")

    load_percent = 0.75  # 75% CPU load target (0.70–0.80 range)
    processes = []

    for _ in range(num_cores):
        p = multiprocessing.Process(target=stress_cpu, args=(load_percent,))
        p.start()
        processes.append(p)

    print(f"Started {num_cores} processes at ~{int(load_percent*100)}% load each. Press Ctrl+C to stop.")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping workers...")
        for p in processes:
            p.terminate()

