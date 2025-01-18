# 🤖 Robotic Cell Management System

Welcome to the **Robotic Cell Management System**! This application simulates a robotic cell where robots and workers collaborate to perform tasks and assemble products in a dynamic environment. This project is ideal for understanding resource allocation, task automation, and process flow in a manufacturing context.

https://github.com/user-attachments/assets/d134b0d0-3f3e-4dfb-8607-2a461a2c8d13

---

## ✨ Key Features

- **Manage Robots**: Add, remove, and track robots and their statuses (e.g., idle, working).
- **Manage Workers**: Add, remove, and track workers and their statuses.
- **Assign Tasks**: Dynamically allocate resources (robots and workers) to tasks based on availability.
- **Assemble Products**: Configure and assign multi-step products to be assembled by the system.
- **Real-Time Status Updates**: Monitor the status of tasks, robots, and workers in real time.
- **Error Handling**: Robust logging and error reporting for smooth operation.

---

## 🛠️ Technologies Used

- **Programming Language**: Python 🐍
- **Data Storage**: JSON files for storing robots, workers, tasks, and products.
- **Logging**: Python’s built-in `logging` module for event and error tracking.
- **Resource Management**: Dynamic allocation and status tracking for robots and workers.

---

## 📚 Libraries Used

- `json`: For reading and writing data files.
- `logging`: For event and error logging.
- `time`: For simulating resource allocation delays.

---

## 📂 Project Structure

```
project-directory/
├── main.py           # Entry point of the program
├── tasks.py          # Core task and product management logic
├── robots.py         # Robot management logic
├── workers.py        # Worker management logic
├── utils.py          # Utility functions (e.g., load and save data)
├── errors.py         # Error handling logic
├── data/
│   ├── robots.json   # Robot data storage
│   ├── workers.json  # Worker data storage
│   ├── tasks.json    # Task data storage
│   └── products.json # Product configurations
└── system.log        # Log file for events and errors
```

---

## 🚀 How to Run the System

### **1. Clone the Repository**
```bash
git clone https://github.com/your-username/robotic-cell-management-system.git
cd robotic-cell-management-system
```

### **2. Install Dependencies**
No external libraries are required. Ensure you have Python 3 installed.

### **3. Start the Application**
Run the following command in the terminal:
```bash
python main.py
```

---

## 🎮 User Guide

Upon starting, the system displays an interactive menu:

### **Available Commands**

| Command           | Description                                |
|-------------------|--------------------------------------------|
| `add_robot`       | Add a new robot to the system              |
| `remove_robot`    | Remove an idle robot from the system       |
| `add_worker`      | Add a new worker to the system             |
| `remove_worker`   | Remove an idle worker from the system      |
| `assign_task`     | Assign a task to available robots/workers  |
| `add_product`     | Add a multi-step product configuration     |
| `assign_product`  | Assign a product for assembly              |
| `check_status`    | Display the status of tasks, robots, workers |
| `complete_task`   | Mark a task as completed                   |
| `quit`            | Exit the system                           |

- 🔧 **add_robot**: Add a new robot to the system.  
- 🗑️ **remove_robot**: Remove an existing robot from the system.  
- 🔧 **add_worker**: Add a new worker to the system.  
- 🗑️ **remove_worker**: Remove an existing worker from the system.  
- 📋 **assign_task**: Assign a task to robots and workers.  
- 🛠️ **add_product**: Add a new product along with its associated steps.  
- 🚀 **assign_product**: Assign a product with multiple steps to the system.  
- 🔍 **check_status**: Display the status of tasks, robots, and workers.  
- ✅ **complete_task**: Mark a task as completed and release its allocated resources.  
- ❌ **quit**: Exit the Robotic Cell Management System.


### **Input Examples**

- **Add a Robot:**
  ```
  🤖 Enter Robot ID: R1
  📊 Enter Robot Status (idle/working): idle
  ```

- **Assign a Task:**
  ```
  📋 Enter Task Name: AssembleEngine
  🤖 Enter Required Robots: 2
  👷 Enter Required Workers: 1
  ```

- **Assign a Product:**
  ```
  🚀 Enter Product Name: CarEngine2
  ```

---

## 📊 Data Management

### **Robots (`robots.json`)**
Stores robot IDs and their statuses:
```json
{
    "R1": "idle",
    "R3": "working",
    "R4": "idle"
}
```

### **Workers (`workers.json`)**
Stores worker IDs and their statuses:
```json
{
    "W1": "idle",
    "W3": "working",
    "W4": "idle"
}
```

### **Tasks (`tasks.json`)**
Tracks the status of tasks:
```json
{
    "Body-Clear": "in progress",
    "Pain": "completed"
}
```

### **Products (`products.json`)**
Defines multi-step product configurations:
```json
{
    "CarEngine2": [
        {"name": "Body-Clear", "robots": 1, "workers": 1},
        {"name": "Pain", "robots": 1, "workers": 2}
    ]
}
```

---

## 🔄 Planned Updates

### Upcoming Features
- **Web Interface**: Replace CLI with a user-friendly web dashboard.
- **Database Integration**: Use SQL or NoSQL databases instead of JSON.
- **Advanced Analytics**: Add resource utilization and task efficiency reports.
- **Simulation Mode**: Visualize task progress in real-time.

---

## 🙌 Contribution

Contributions are welcome! Follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

---

## 📜 License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## ❤️ Acknowledgments

Thanks to all contributors and users who support this project! If you find this project helpful, don’t forget to give it a ⭐ on GitHub!

