class Todo:
    def __init__(self, taskName, isCompleted=False):
        self.taskName = taskName
        self.isCompleted = isCompleted 

class TodoList:
    def __init__(self):
        self.todos = []

    def addTodo(self, Todo):
        self.todos.append(Todo)
        print(f"Task {Todo.taskName} Added Successfully \n")

    def removeTodo(self, index):
        deletedTask = self.todos.pop(index)
        print(f"Task {deletedTask.taskName} Deleted Successfully \n")


    def viewAllTodos(self):
        for i in self.todos:
            print(f" id = {self.todos.index(i)}")
            print(f" taskName = {i.taskName}")
            print(f" isCompleted = {i.isCompleted} \n\n")
    
    def updateTodo(self, index):
        if self.todos[index].isCompleted == False:
            self.todos[index].isCompleted = True
        else:
            self.todos[index].isCompleted = False
        print(f"Task {self.todos[index].taskName} Updated Successfully \n")


def main():
    t = TodoList()
    print("\n\n------------------------Todo App------------------------\n\n")
    while True:
        print('''press the menu index:
    1. Add a task
    2. View all tasks
    3. Update task
    4. Remove Task
    5. Exit\n''')
        choice = int(input("Enter your choice:"))
        match choice:
            case 1:
                t.addTodo(Todo(input("Enter the Task Name: ")))
            case 2:
                t.viewAllTodos()
            case 3:
                t.updateTodo(int(input("Enter the Task ID: ")))
            case 4:
                t.removeTodo(int(input("Enter the Task ID: ")))
            case _:
                break


if __name__ == "__main__":
    main()