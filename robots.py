from utils import load_data, save_data

ROBOT_FILE = "data/robots.json"

def add_robot(robot_id, status):
    robots = load_data(ROBOT_FILE)
    if robot_id in robots:
        print(f"⚠️ Robot {robot_id} already exists.")
    else:
        robots[robot_id] = status
        save_data(ROBOT_FILE, robots)
        print(f"✅ Robot {robot_id} added with status '{status}'.")

def remove_robot(robot_id):
    robots = load_data(ROBOT_FILE)
    if robot_id in robots:
        if robots[robot_id] == "idle":
            del robots[robot_id]
            save_data(ROBOT_FILE, robots)
            print(f"✅ Robot {robot_id} removed.")
        else:
            print(f"⚠️ Error: Cannot remove Robot {robot_id} (currently assigned to a task).")
    else:
        print(f"⚠️ Robot {robot_id} does not exist.")
