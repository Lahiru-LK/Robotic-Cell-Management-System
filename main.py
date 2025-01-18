from tasks import assign_task, check_task_status, complete_task, add_product, assign_product
from robots import add_robot, remove_robot
from workers import add_worker, remove_worker
from errors import handle_error
from utils import log_event, log_error

VALID_COMMANDS = {"add_robot", "remove_robot", "add_worker", "remove_worker",
                  "assign_task", "check_status", "complete_task",
                  "add_product", "assign_product", "quit"}


def display_menu():
    """Display the main menu."""
    print("\n","🟩" * 40)
    print("\n✨ === Robotic Cell Management System === ✨")
    print("🤖 Available Commands:","\n")
    print("🔧 - add_robot      : Add a new robot")
    print("🗑️  - remove_robot   : Remove an existing robot")
    print("🔧 - add_worker     : Add a new worker")
    print("🗑️  - remove_worker  : Remove an existing worker")
    print("📋 - assign_task    : Assign a task to robots and workers")
    print("🛠️  - add_product    : Add a new product with steps")
    print("🚀 - assign_product : Assign a product with multiple steps")
    print("🔍 - check_status   : Display the status of tasks, robots, and workers")
    print("✅ - complete_task  : Mark a task as completed and release resources")
    print("❌ - quit           : Exit the system")
    print("\n","🟩" * 40,"\n")


def main():
    """Main program loop."""
    print("🌟 Welcome to the Robotic Cell Management System! 🌟")
    log_event("System started.")

    while True:
        display_menu()
        command = input("👉 Enter Command: ").strip().lower()

        if command not in VALID_COMMANDS:
            print(f"⚠️ Invalid command: '{command}'. Please select from the menu.")
            log_error(f"Invalid command entered: {command}")
            continue

        try:
            if command == "add_robot":
                robot_id = input("🤖 Enter Robot ID: ").strip()
                status = input("📊 Enter Robot Status (idle/working): ").strip()
                add_robot(robot_id, status)
                log_event(f"Robot added: {robot_id} with status {status}")

            elif command == "remove_robot":
                robot_id = input("🗑️ Enter Robot ID to remove: ").strip()
                remove_robot(robot_id)
                log_event(f"Robot removed: {robot_id}")

            elif command == "add_worker":
                worker_id = input("👷 Enter Worker ID: ").strip()
                status = input("📊 Enter Worker Status (idle/working): ").strip()
                add_worker(worker_id, status)
                log_event(f"Worker added: {worker_id} with status {status}")

            elif command == "remove_worker":
                worker_id = input("🗑️ Enter Worker ID to remove: ").strip()
                remove_worker(worker_id)
                log_event(f"Worker removed: {worker_id}")

            elif command == "assign_task":
                task_name = input("📋 Enter Task Name: ").strip()
                required_robots = int(input("🤖 Enter Required Robots: "))
                required_workers = int(input("👷 Enter Required Workers: "))
                assign_task(task_name, required_robots, required_workers)
                log_event(f"Task assigned: {task_name} requiring {required_robots} robots and {required_workers} workers")

            elif command == "add_product":
                product_name = input("📦 Enter Product Name: ").strip()
                num_steps = int(input("🛠️ Enter Number of Steps: "))
                product_steps = []

                for i in range(num_steps):
                    print(f"📋 Step {i + 1}:")
                    step_name = input("🔧 Enter Step Name: ").strip()
                    robots = int(input("🤖 Enter Required Robots: "))
                    workers = int(input("👷 Enter Required Workers: "))
                    product_steps.append({"name": step_name, "robots": robots, "workers": workers})

                add_product(product_name, product_steps)
                log_event(f"Product added: {product_name} with {num_steps} steps")

            elif command == "assign_product":
                product_name = input("🚀 Enter Product Name: ").strip()
                assign_product(product_name)
                log_event(f"Product assigned: {product_name}")

            elif command == "check_status":
                print("\n🔍 System Status:")
                check_task_status()

            elif command == "complete_task":
                task_name = input("✅ Enter Task Name to complete: ").strip()
                complete_task(task_name)
                log_event(f"Task completed: {task_name}")

            elif command == "quit":
                print("\n❌ Thank you for using the Robotic Cell Management System. Goodbye!")
                log_event("System terminated.")
                break

        except Exception as e:
            handle_error(e)
            log_error(f"Error occurred: {e}")


if __name__ == "__main__":
    main()
