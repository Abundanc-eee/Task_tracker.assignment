NAME: OLADIPUPO OLAYINKA ABUNDANCE

MATRIC NUMBER: 24/14647

DEPARTMENT: COMPUTER SCIENCE

The assignment says that we should pick any project of our choice and explain the full SDLC of that project. Implememt the code and push it to github.

Therefore, below is the full SDLC explanation of my project

I created a Task Tracker CLI that can help track tasks and maintain orderliness with tasks done and the ones undone

SDLC Documentation: Task Tracker CLI
1. Requirements Analysis Phase
The objective is to build a lightweight, local task management system.
Functional Requirements:
oAdd new tasks with a text description.
oList all existing tasks showing their ID and completion status.
oMark a specific task as "done" using its unique ID.
Non-Functional Requirements:
oPersistence: Data must survive after the program closes.
oSimplicity: No external database engines (like MySQL) required.
2. Design Phase (Nomenclature)
During this phase, the technical “dictionary” for the project was designed to ensure that the codes are organized.
Primary Class:TaskTracker (The engine that runs the logic).
Data Structure: A List of Dictionaries named task_list.
Data Attributes:
oid: An integer for unique identification.
odescription: A string containing the task text.
ostatus: A string with two possible states: "pending" or "done".
Storage Component: A JSON file named tasks_db.json.
3. Implementation Phase (Coding)
The code was written in Python to fulfill the design. Key methods implemented include:
_load_tasks(): Reads from tasks_db.json.
_save_tasks(): Writes the task_list back to the JSON file.
add_task(description): Appends a new dictionary to the list.
complete_task(task_id): Searches the list for a matching id and updates its status.
4. Testing Phase
Testing was performed via the command line to verify the logic:
1.Creation Test: Verified that running add created the tasks_db.json file.
2.Integrity Test: Verified that list correctly parsed the JSON and displayed the [✔] or [☐] icons based on the status value.
3.Boundary Test: Verified that the id increments correctly for each new task.
5. Deployment & Maintenance
Deployment: The script is distributed as a single .py file.
Maintenance: Future updates (like a "Delete" function) will follow the same nomenclature, ensuring the task_list and tasks_db.json remain the single sources of truth.

Below is the repository link to the Task-tracker project I pushed to github:
https://github.com/Abundanc-eee/Task_tracker.assignment.git

