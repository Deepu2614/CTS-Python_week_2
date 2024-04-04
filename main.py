
class Todo:
    def __init__(self, taskName, isCompleted=False):
        self.taskName = taskName
        self.isCompleted = isCompleted 

class TodoList:
    def __init__(self):
        self.todos = []

    def addTodo(self, Todo):
        self.todos.append(Todo)

    def updateTodo(self, index):
        if self.todos[index].isCompleted == False:
            self.todos[index].isCompleted = True
        else:
            self.todos[index].isCompleted = False
    
    def removeTodo(self, index):
        self.todos.pop(index)


    