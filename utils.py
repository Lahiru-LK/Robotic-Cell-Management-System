import json
import logging

def load_data(file_path):
    try:
        with open(file_path, "r") as file:
            data = file.read().strip()
            return json.loads(data) if data else {}
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print(f"⚠️ Error: The file {file_path} is not a valid JSON file. Resetting it to an empty state.")
        save_data(file_path, {})
        return {}

def save_data(file_path, data):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)


# Configure logging
logging.basicConfig(
    filename="system.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_event(message):
    """Log an informational event."""
    logging.info(message)
    print(f"📝 Log: {message}")  # Optional: Print to console for debugging

def log_error(message):
    """Log an error event."""
    logging.error(message)
    print(f"⚠️ Log Error: {message}")  # Optional: Print to console for debugging
