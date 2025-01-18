import time
from utils import load_data, save_data

PRODUCT_FILE = "data/products.json"
TASK_FILE = "data/tasks.json"
ROBOT_FILE = "data/robots.json"
WORKER_FILE = "data/workers.json"

def assign_task(task_name, required_robots, required_workers):
    """Assign a task to the available robots and workers."""
    tasks = load_data(TASK_FILE)

    max_wait_time = 10  # Max number of iterations to wait for resources
    wait_time = 0  # Counter for waiting iterations

    while True:
        robots = load_data(ROBOT_FILE)  # Refresh robot data
        workers = load_data(WORKER_FILE)  # Refresh worker data

        available_robots = [r for r, s in robots.items() if s == "idle"]
        available_workers = [w for w, s in workers.items() if s == "idle"]

        # Debugging assistance: Print available resources
        print(f"Available Robots: {available_robots}")
        print(f"Available Workers: {available_workers}")

        if len(available_robots) >= required_robots and len(available_workers) >= required_workers:
            # Assign resources
            for i in range(required_robots):
                robots[available_robots[i]] = "working"
            for i in range(required_workers):
                workers[available_workers[i]] = "working"

            tasks[task_name] = "in progress"
            save_data(ROBOT_FILE, robots)
            save_data(WORKER_FILE, workers)
            save_data(TASK_FILE, tasks)
            print(f"✅ Task '{task_name}' started.")
            break

        wait_time += 1
        if wait_time >= max_wait_time:
            print(f"⚠️ Resources are still not available after waiting for {max_wait_time * 2} seconds.")
            break

        print("⏳ Waiting for resources to be freed...")
        time.sleep(2)  # Simulate waiting time



def complete_task(task_name):
    """Mark a task as completed and release resources."""
    tasks = load_data(TASK_FILE)
    robots = load_data(ROBOT_FILE)
    workers = load_data(WORKER_FILE)

    if task_name in tasks and tasks[task_name] == "in progress":
        tasks[task_name] = "completed"
        for robot_id, status in robots.items():
            if status == "working":
                robots[robot_id] = "idle"
        for worker_id, status in workers.items():
            if status == "working":
                workers[worker_id] = "idle"
        save_data(TASK_FILE, tasks)
        save_data(ROBOT_FILE, robots)
        save_data(WORKER_FILE, workers)
        print(f"✅ Task '{task_name}' marked as completed. Resources released.")

        # Notify if all tasks are completed
        if all(status == "completed" for status in tasks.values()):
            print("🎉 All tasks have been completed!")
    else:
        print(f"⚠️ Task '{task_name}' not found or already completed.")


def check_task_status():
    tasks = load_data(TASK_FILE)
    robots = load_data(ROBOT_FILE)
    workers = load_data(WORKER_FILE)

    print("Task Status:")
    for task, status in tasks.items():
        print(f"- {task}: {status}")

    print("\nRobots:")
    for robot, status in robots.items():
        print(f"- {robot}: {status}")

    print("\nWorkers:")
    for worker, status in workers.items():
        print(f"- {worker}: {status}")


PRODUCT_FILE = "data/products.json"


def add_product(product_name, product_steps):
    """Add a new product with steps defined by the user."""
    products = load_data(PRODUCT_FILE)

    if product_name in products:
        print(f"⚠️ Product '{product_name}' already exists.")
        return

    products[product_name] = product_steps
    save_data(PRODUCT_FILE, products)
    print(f"✅ Product '{product_name}' added successfully.")


def assign_product(product_name):
    """Assign a product consisting of multiple steps."""
    products = load_data(PRODUCT_FILE)
    robots = load_data(ROBOT_FILE)
    workers = load_data(WORKER_FILE)

    if product_name not in products:
        print(f"⚠️ Error: Product '{product_name}' not found.")
        return

    available_robots = sum(1 for r in robots.values() if r == "idle")
    available_workers = sum(1 for w in workers.values() if w == "idle")

    product_steps = products[product_name]
    max_robots = max(step["robots"] for step in product_steps)
    max_workers = max(step["workers"] for step in product_steps)

    if available_robots < max_robots or available_workers < max_workers:
        print(f"⚠️ Error: Not enough resources to assign product '{product_name}'.")
        print(f"Required: {max_robots} robots, {max_workers} workers.")
        print(f"Available: {available_robots} robots, {available_workers} workers.")
        return

    for step in product_steps:
        print(f"Starting step: {step['name']}...")
        assign_task(step["name"], step["robots"], step["workers"])
    print(f"🎉 Product '{product_name}' has been successfully assembled!")

