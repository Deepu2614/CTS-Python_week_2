# to-do class with 2 attributes -> taskName, isCompleted
class Todo:
    def __init__(self, taskName, isCompleted=False):
        self.taskName = taskName
        self.isCompleted = isCompleted 

# todo list class with all manipulation methods
class TodoList:
    def __init__(self):
        self.todos = []

    # to add todos to todos list
    def addTodo(self, Todo):
        self.todos.append(Todo)
        print(f"Task {Todo.taskName} Added Successfully \n")

    # to remove todos to todos list
    def removeTodo(self, index):
        deletedTask = self.todos.pop(index)
        print(f"Task {deletedTask.taskName} Deleted Successfully \n")

    # to view all todos
    def viewAllTodos(self):
        for i in self.todos:
            print(f" id = {self.todos.index(i)}")
            print(f" taskName = {i.taskName}")
            print(f" isCompleted = {i.isCompleted} \n\n")
    
    # to update todo
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

    def updateTodo(self, index):
        if self.todos[index].isCompleted == False:
            self.todos[index].isCompleted = True
        else:
            self.todos[index].isCompleted = False
    
    def removeTodo(self, index):
        self.todos.pop(index)


    def viewAllTodos(self):
        for i in t.todos:
            print(f" id = {t.todos.index(i)}")
            print(f" taskName = {i.taskName}")
            print(f" isCompleted = {i.isCompleted}")



if __name__ == "__main__":
    main()

