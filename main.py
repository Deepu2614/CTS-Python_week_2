#init

class Todo:
    def __init__(self, taskName, isCompleted=False):
        self.taskName = taskName
        self.isCompleted = isCompleted 

class TodoList:
    def __init__(self):
        self.todos = []

    def addTodo(self, Todo):
        self.todos.append(Todo)


# t= TodoList()
# t.addTodo(Todo("Add choco"))
# t.addTodo(Todo("Add milk"))
# for i in t.todos:
#     print(i.taskName)
    