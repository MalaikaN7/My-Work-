from datetime import datetime
# Create a list to store users and tasks.
user_info = []
task_info = []

# Create variables to store user infor and asks in their respective txt files.
user_info = "user.txt"
task_info = "task.txt"

# To get user log ins and check if the username and password are correct
valid_user = False
while not valid_user:
    username = input("Please enter your username: ").strip()
    password = input("Please enter your password: ").strip()

    with open(user_info, "r") as file_:
        for line in file_:
            stored_user, stored_pass = line.strip().split(", ")
            if username == stored_user and password == stored_pass:
                valid_user = True
                break

        if valid_user:
            print(f"Welcome, {username}.")
            break
        else:
            print("Invalid user or password, please try again.")

while True:
    if username == "admin":
        print("r - register a user")
        print("a - add task")
        print("va - view all tasks")
        print("vm - view my tasks")
        print("ds - Display Stats")
        print("e - exit")
    else:
        print("a - add task")
        print("r - va - view all tasks")
        print("vm - view my tasks")
        print("e - exit")

# Main menu for the users actions.
    menu = input("Select one of the options to proceed: ").strip().lower()
    if menu == "r" and username == "admin":
        new_user = input("Enter the name of new user: ").strip()
        while True:
            user_pass = input("Please enter a password: ").strip()
            conf_pass = input("Please confirm your password: ").strip()

            if user_pass == conf_pass:
                with open(user_info, 'a') as user_file:
                    user_file.write(f"\n{new_user}, {user_pass}")
                    print(f"{new_user}, registered successfully!")
                    print("Password confirmation succesful.")
                    break

            else:
                print("Passwords don't match, please try again.")

# Add a new task.
    elif menu == 'a':
        task_assi_to = input("Please enter the name who the task is assigned to:").strip()
        task_title = input("Please enter the title of the task:").strip()
        task_description = input("Please enter the description of the task:").strip()
        task_date = input("Please enter the tasks due date:").strip()
        current_date = datetime.today().date()
        print("Todays date is: ", current_date)

        task_finished = input("Is the task completed yes/no:").strip()
        if task_finished == "no":
            print("Task is not completed.")

# Save the task details to task file.
            with open(task_info, "a") as file_2:
                file_2.write(f"{task_assi_to}, {task_title}, {task_description}, {task_date}, {current_date}, {task_finished}")
            print("\n"f"{task_assi_to}, {task_title}, {task_description}, {task_date}, {current_date}, {task_finished}")
            print("Task added successfully.")

# Menu option to view all tasks
    elif menu == "va":
        print("\nViewing all tasks:")
        with open(task_info, "r") as file_2:
            for line in file_2:
                task_det = line.strip().split(", ")
                if len(task_det) == 6:
                    task_assi_to, task_title, task_description, task_date, current_date, task_finished = task_det
                    print("\n_________________________________________")
                    print(f"Task: {task_title}\n")
                    print(f"Task assigned to: {task_assi_to}\n")
                    print(f"Task description: {task_description}\n")
                    print(f"The current date: {current_date}\n")
                    print(f"Task due date: {task_date}\n")
                    print(f"Task completed: {task_finished}")
                    print("_________________________________________\n")
                else:
                    print("Error: A line in the task file does not match the expected number of elements.")

# View tasks that are assigned to the log-in user.
    elif menu == "vm":
        print(f"\n View tasks assigned to: {username}")
        no_alloc_task = True
        with open(task_info) as file_2:
            for line in file_2:
                task_det = line.strip().split(", ")
                if len(task_det) == 6 and task_det[0] == username:
                    no_alloc_task = False 
                    task_assi_to, task_title, task_description, task_date, curent_date, task_finished = task_det
                    print("\n_________________________________________")
                    print(f"Task: {task_title}\n")
                    print(f"Task assigned to: {task_assi_to}\n")
                    print(f"Task description: {task_description}\n")
                    print(f"The current date: {curent_date}\n")
                    print(f"Task due date: {task_date}\n")
                    print(f"Task completed: {task_finished}")
                    print("_________________________________________\n")
            if no_alloc_task:
                print("no tasks allocated to user")
    # Menu option for admin to display stats.
    elif menu == "ds" and username == "admin":
        with open(task_info, "r") as file_3, open(user_info, "r") as file_4:
            lines1 = len(file_3.readlines())
            print(f"There are {lines1} tasks in the task file.")

            lines2 = len(file_4.readlines())
            print(f"There are {lines2} users in the user file.")

# Exit option to stop the program
    elif menu == 'e':
        print('Goodbye!!!')
        break

# Message to relay invalid inputs.
    else:
        print("You have entered an invalid input. Please try again")
