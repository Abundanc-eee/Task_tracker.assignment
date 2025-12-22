import json
import os
import sys

class TaskTracker:
    """
    A simple CLI tool to manage tasks.
    Nomenclature: 
    - tasks_db: The JSON storage file
    - task_list: The in-memory list of dictionaries
    """
    def __init__(self, filename='tasks_db.json'):
        self.filename = filename
        self.task_list = self._load_tasks()

    def _load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return json.load(f)
        return []

    def _save_tasks(self):
        with open(self.filename, 'w') as f:
            json.dump(self.task_list, f, indent=4)

    def add_task(self, description):
        task_id = len(self.task_list) + 1
        new_task = {
            "id": task_id,
            "description": description,
            "status": "pending"
        }
        self.task_list.append(new_task)
        self._save_tasks()
        print(f"Task added: {description}")

    def list_tasks(self):
        if not self.task_list:
            print("No tasks found.")
            return
        for task in self.task_list:
            status_icon = "✔" if task['status'] == 'done' else "☐"
            print(f"{task['id']}. [{status_icon}] {task['description']}")

    def complete_task(self, task_id):
        for task in self.task_list:
            if task['id'] == task_id:
                task['status'] = 'done'
                self._save_tasks()
                print(f"Task {task_id} marked as complete.")
                return
        print("Task ID not found.")

# Usage Implementation
if __name__ == "__main__":
    tracker = TaskTracker()
    # Simple CLI argument routing
    if len(sys.argv) < 2:
        print("Usage: python task_tracker.py [add/list/done] [args]")
    elif sys.argv[1] == "add":
        tracker.add_task(" ".join(sys.argv[2:]))
    elif sys.argv[1] == "list":
        tracker.list_tasks()
    elif sys.argv[1] == "done":
        tracker.complete_task(int(sys.argv[2]))