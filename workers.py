from utils import load_data, save_data

WORKER_FILE = "data/workers.json"

def add_worker(worker_id, status):
    workers = load_data(WORKER_FILE)
    if worker_id in workers:
        print(f"⚠️ Worker {worker_id} already exists.")
    else:
        workers[worker_id] = status
        save_data(WORKER_FILE, workers)
        print(f"✅ Worker {worker_id} added with status '{status}'.")

def remove_worker(worker_id):
    workers = load_data(WORKER_FILE)
    if worker_id in workers:
        if workers[worker_id] == "idle":
            del workers[worker_id]
            save_data(WORKER_FILE, workers)
            print(f"✅ Worker {worker_id} removed.")
        else:
            print(f"⚠️ Error: Cannot remove Worker {worker_id} (currently assigned to a task).")
    else:
        print(f"⚠️ Worker {worker_id} does not exist.")
