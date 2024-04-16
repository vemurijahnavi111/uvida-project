#!/usr/bin/env python
# coding: utf-8

# In[1]:


class ToDoList:
    def __init__(self):
        self.tasks = self.load_from_file()

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully.")

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print("Task removed successfully.")
        else:
            print("Task not found.")

    def display_tasks(self):
        if self.tasks:
            print("Your To-Do List:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("Your To-Do List is empty.")

    def save_to_file(self):
        filename = "todo_list.txt"
        with open(filename, "w") as f:
            for task in self.tasks:
                f.write(task + "\n")
        print(f"To-Do List saved to {filename}.")

    def load_from_file(self):
        filename = "todo_list.txt"
        try:
            with open(filename, "r") as f:
                tasks = [line.strip() for line in f.readlines()]
            print(f"To-Do List loaded from {filename}.")
            return tasks
        except FileNotFoundError:
            print("To-Do List file not found.")
            return []

def main():
    to_do_list = ToDoList()

    while True:
        print("\n1. Add Task")
        print("2. Remove Task")
        print("3. Display Tasks")
        print("4. Save To-Do List to File")
        print("5. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            to_do_list.add_task(task)
        elif choice == '2':
            task = input("Enter the task to remove: ")
            to_do_list.remove_task(task)
        elif choice == '3':
            to_do_list.display_tasks()
        elif choice == '4':
            to_do_list.save_to_file()
        elif choice == '5':
            to_do_list.save_to_file()
            print("Quitting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()


# In[ ]:




