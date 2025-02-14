from datetime import datetime

# File names for storing user and task data
user_info = "user.txt"
task_info = "task.txt"
task_overview_file = "task_overview.txt"
user_overview_file = "user_overview.txt"


# Function to register a new user
def reg_user():
    """
    Registers a new user by prompting for a username and password.
    Ensures that the username does not already exist and that the
    password is confirmed correctly.
    """
    new_user = input("Enter the name of the new user: ").strip()

    # Check if the username already exists
    with open(user_info, "r") as file_:
        for line in file_:
            stored_user, _ = line.strip().split(", ")
            if new_user == stored_user:
                print(f"Error: Username '{new_user}' already exists.")
                return

    # Ask for password until both entries match
    while True:
        user_pass = input("Please enter a password: ").strip()
        conf_pass = input("Please confirm your password: ").strip()

        if user_pass == conf_pass:
            with open(user_info, 'a') as user_file:
                user_file.write(f"\n{new_user}, {user_pass}")
            print(f"{new_user} registered successfully!")
            return
        else:
            print("Passwords don't match, please try again.")


# Function to add a new task
def add_task():
    """
    Adds a new task by prompting for task details such as the assignee, title,
    description, due date, and whether the task is completed.
    """
    task_assi_to = input("Please enter the name of the person the task is \
assigned to: ").strip()
    task_title = input("Please enter the title of the task: ").strip()
    task_description = input("Please enter the description of the task: ").strip()
    task_date = input("Please enter the task's due date (YYYY-MM-DD): ").strip()
    current_date = datetime.today().date()  # Get current date
    task_finished = input("Is the task completed (yes/no): ").strip().lower()

    if task_finished != "yes":
        task_finished = "no"

    # Append task details to the task file
    with open(task_info, "a") as file_2:
        file_2.write(f"{task_assi_to}, {task_title}, {task_description}, {task_date}, {current_date}, {task_finished}\n")

    print(f"Task added successfully for {task_assi_to}.")


# Function to view all tasks
def view_all():
    """
    Displays all tasks stored in the task file, including task details such
    as assignee, title, description, current date, due date, and completion status.
    """
    print("\nViewing all tasks:")
    with open(task_info, "r") as file_2:
        for line in file_2:
            task_det = line.strip().split(", ")
            if len(task_det) == 6:
                task_assi_to, task_title, task_description, task_date, current_date, task_finished = task_det
                print("\n_________________________________________")
                print(f"Task: {task_title}\nAssigned to: {task_assi_to}\nDescription: {task_description}\n"
                      f"Current date: {current_date}\nDue date: {task_date}\nCompleted: {task_finished}")
                print("_________________________________________")


# Function to view tasks assigned to the logged-in user
def view_mine(username):
    """
    Displays tasks assigned specifically to the logged-in user.
    Allows the user to modify a task (either mark it as complete or edit it).
    """
    tasks = []
    print(f"\nView tasks assigned to: {username}")
    with open(task_info, "r") as file_2:
        for idx, line in enumerate(file_2):
            task_det = line.strip().split(", ")
            if len(task_det) == 6 and task_det[0] == username:
                tasks.append((idx, task_det))

    if tasks:
        # Display user-specific tasks
        for i, task in tasks:
            task_assi_to, task_title, task_description, task_date, current_date, task_finished = task
            print(f"\nTask {i + 1}: {task_title}\nAssigned to: {task_assi_to}\nDescription: {task_description}\n"
                  f"Due date: {task_date}\nCompleted: {task_finished}")

        # Prompt user to modify a specific task
        task_num = int(input("\nSelect a task number to modify (or -1 to return to main menu): "))
        if task_num == -1:
            return

        task_to_modify = tasks[task_num - 1][1]
        modify_task(task_to_modify, task_num)
    else:
        print("No tasks assigned to you.")


# Function to modify a specific task (mark complete or edit)
def modify_task(task, task_num):
    """
    Modifies a selected task by either marking it as complete or editing
    its details, such as changing the assignee or due date.
    """
    task_assi_to, task_title, task_description, task_date, current_date, task_finished = task

    if task_finished == "yes":
        print("This task is already completed and cannot be edited.")
        return

    # Prompt user for action: complete or edit the task
    user_action = input("Would you like to (c) mark complete or (e) edit the task? ").strip().lower()
    if user_action == "c":
        task_finished = "yes"
        update_task_file(task_num, task_assi_to, task_title, task_description, task_date, current_date, task_finished)
    elif user_action == "e":
        task_assi_to = input(f"Enter the new person for the task (or press Enter to keep {task_assi_to}): ").strip() or task_assi_to
        task_date = input(f"Enter the new due date (YYYY-MM-DD) (or press Enter to keep {task_date}): ").strip() or task_date
        update_task_file(task_num, task_assi_to, task_title, task_description, task_date, current_date, task_finished)


# Function to update the task file after modifying a task
def update_task_file(task_num, task_assi_to, task_title, task_description, task_date, current_date, task_finished):
    """
    Updates the task file by replacing the modified task at the specified index.
    """
    with open(task_info, "r") as file_2:
        tasks = file_2.readlines()

    # Update the task at the given index
    tasks[task_num - 1] = f"{task_assi_to}, {task_title}, {task_description}, {task_date}, {current_date}, {task_finished}\n"

    # Write updated tasks back to the file
    with open(task_info, "w") as file_2:
        file_2.writelines(tasks)

    print("Task updated successfully.")


# Function to generate reports
def generate_reports():
    """
    Generates two reports: a task overview and a user overview.
    The reports include information on total tasks, completed tasks,
    overdue tasks, and the performance of each user.
    """
    task_report = []
    user_report = []
    total_tasks = completed_tasks = overdue_tasks = 0
    today = datetime.today().date()

    # Calculate task statistics
    with open(task_info, "r") as task_file:
        tasks = task_file.readlines()
        total_tasks = len(tasks)
        for task in tasks:
            task_assi_to, task_title, task_description, task_due_date, current_date, task_finished = task.strip().split(", ")
            if task_finished == "yes":
                completed_tasks += 1
            if task_finished == "no" and datetime.strptime(task_due_date, '%Y-%m-%d').date() < today:
                overdue_tasks += 1

    # Prepare task overview report
    task_report.append(f"Total tasks: {total_tasks}")
    task_report.append(f"Completed tasks: {completed_tasks}")
    task_report.append(f"Uncompleted tasks: {total_tasks - completed_tasks}")
    task_report.append(f"Overdue tasks: {overdue_tasks}")
    task_report.append(f"Percentage of overdue tasks: {overdue_tasks / total_tasks * 100:.2f}%\n")

    with open(task_overview_file, "w") as file_:
        file_.write("\n".join(task_report))

    # Prepare user overview report
    with open(user_info, "r") as user_file:
        users = user_file.readlines()

    user_report.append(f"Total users: {len(users)}")
    user_report.append(f"Total tasks: {total_tasks}")
    for user in users:
        username, _ = user.strip().split(", ")
        user_tasks = [task for task in tasks if task.startswith(username)]
        user_task_count = len(user_tasks)
        completed_user_tasks = sum(1 for task in user_tasks if "yes" in task)
        overdue_user_tasks = sum(1 for task in user_tasks if "no" in task and today > datetime.strptime(task.split(", ")[3], '%Y-%m-%d').date())

        user_report.append(f"\n{username} has {user_task_count} tasks ({user_task_count / total_tasks * 100:.2f}% of all tasks).\n")
        user_report.append(f"{completed_user_tasks} completed tasks.\n")
        user_report.append(f"{user_task_count - completed_user_tasks} uncompleted tasks.\n")
        user_report.append(f"{overdue_user_tasks} overdue tasks.\n")

    with open(user_overview_file, "w") as file_:
        file_.write("\n".join(user_report))

    print("Reports generated successfully.")


# Main log-in program
def log_in():
    """
    Handles the login process, prompting the user for a username and password.
    Admin users have access to additional options, such as registering new users
    and generating reports.
    """
    valid_user = False
    while not valid_user:
        username = input("Please enter your username: ").strip()
        password = input("Please enter your password: ").strip()

        # Validate user credentials
        with open(user_info, "r") as file_:
            for line in file_:
                stored_user, stored_pass = line.strip().split(", ")
                if username == stored_user and password == stored_pass:
                    valid_user = True
                    break

        if valid_user:
            print(f"Welcome, {username}.")
        else:
            print("Invalid username or password, please try again.")

    # Display menu options based on the user role
    while True:
        if username == "admin":
            print("r - register a user\n"
                  "a - add task\n"
                  "va - view all tasks\n"
                  "vm - view my tasks\n"
                  "gr - generate reports\n"
                  "ds - display stats\n"
                  "e - exit")
        else:
            print("a - add task\n"
                  "va - view all tasks\n"
                  "vm - view my tasks\n"
                  "e - exit")

        # Handle user selection
        menu = input("Select an option: ").strip().lower()

        if menu == "r" and username == "admin":
            reg_user()
        elif menu == "a":
            add_task()
        elif menu == "va":
            view_all()
        elif menu == "vm":
            view_mine(username)
        elif menu == "gr" and username == "admin":
            generate_reports()
        elif menu == "ds" and username == "admin":
            # Generate reports if they do not exist
            generate_reports()
            with open(task_overview_file, "r") as file_:
                print(file_.read())
            with open(user_overview_file, "r") as file_:
                print(file_.read())
        elif menu == "e":
            print("Goodbye!")
            break

# Main program entry point
if __name__ == "__main__":
    log_in()
