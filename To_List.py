# Define a class TodoList to represent a to-do list
class TodoList:
    # Constructor method initializes an empty list to store tasks
    def __init__(self):
        self.tasks = []

    # Method to add a task to the to-do list
    def add_task(self, task):
        self.tasks.append(task)  # Append the task to the list
        with open("todo.txt", "a") as file:
            file.write(task + '\n')  # Write the task to the file
        print("Task added successfully!")  # Print a success message

    # Method to view tasks in the to-do list
    def view_tasks(self):
        if self.tasks:  # Check if the list is not empty
            print("Your To-Do List:")
            # Iterate over tasks and print each task along with its index
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("Your to-do list is empty!")  # Print a message if the list is empty

    # Method to mark a task as completed
    def mark_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):  # Check if the task index is valid
            # Append "- Completed" to the task description to mark it as completed
            self.tasks[task_index - 1] += " - Completed"
            print("Task marked as completed!")  # Print a success message
        else:
            print("Invalid task index!")  # Print an error message for invalid index

    # Method to remove a task from the to-do list
    def remove_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):  # Check if the task index is valid
            del self.tasks[task_index - 1]  # Delete the task from the list
            print("Task removed successfully!")  # Print a success message
        else:
            print("Invalid task index!")  # Print an error message for invalid index


# Define the main function to run the to-do list application
def main():
    todo_list = TodoList()  # Create an instance of TodoList
    # Load tasks from the file if it exists
    try:
        with open("todo.txt", "r") as file:
            todo_list.tasks = file.readlines()
    except FileNotFoundError:
        pass

    while True:  # Main loop for menu-driven interaction
        print("\n===== To-Do List Application =====")
        # Display menu options
        print("1. Add a task")
        print("2. View tasks")
        print("3. Mark task as completed")
        print("4. Remove task")
        print("5. Exit")

        choice = input("Enter your choice: ")  # Prompt user for choice

        # Execute corresponding action based on user's choice
        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            task_index = int(input("Enter the index of the task to mark as completed: "))
            todo_list.mark_completed(task_index)
        elif choice == '4':
            task_index = int(input("Enter the index of the task to remove: "))
            todo_list.remove_task(task_index)
        elif choice == '5':
            print("Exiting...")  # Print exit message
            # Save tasks to the file before exiting
            with open("todo.txt", "w") as file:
                file.writelines(todo_list.tasks)
            break  # Exit the loop and terminate the program
        else:
            print("Invalid choice! Please enter a valid option.")  # Print error message for invalid choice


# Check if the script is run directly
if __name__ == "__main__":
    main()  # Call the main function to start the application
