dashboard = """
=====TO-DO List Menu=====
    1. Add task
    2. See all Tasks
    3. Remove Task
    4. Update Task
Enter your Choice
    """
menu=input(dashboard)

taskDictionary = {}
def addTask():
    taskTitle= input("Enter your task title: ")
    taskDescription= input("Enter task description: ")
    taskDictionary = {k:v for (k,v) in zip(taskTitle, taskDescription)}
    print("task successfully added ")
    nextMenuOption=input(dashboard)
    if(nextMenuOption=="1"):
        addTask()
    elif(nextMenuOption=="2"):
        allTask()
    elif(nextMenuOption=="3"):
        removeTask()
    elif(nextMenuOption=="4"):
        updateTask()
    else:
        print("invalid menu option")

def removeTask():
    print("from remove task")

def updateTask():
    print("from update task")

def allTask():
    print(taskDictionary)

if(menu=="1"):
    addTask()
elif(menu=="2"):
    allTask()
elif(menu=="3"):
    removeTask()
elif(menu=="4"):
    updateTask()