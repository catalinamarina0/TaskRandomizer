import random
import json
import sys

def choices():
    print("1. Randomize task")
    print("2. Add task")
    print("3. Task done")
    print("4. View list of tasks")
    print("5. Exit")
    print("")
    number = input("Input number: ")
    return number

def inputTask():
    task = input("Task: ")
    return task

def storeTasks(tasks):
    json.dump(tasks,open("etc/tasks.json","w"))

def getTasks():
    try:
        tasks = json.load(open("etc/tasks.json","r"))
    except:
        tasks = {}
    return tasks

def addTask(tasks):
    task = inputTask()
    weight = int(input("Weight: "))
    tasks[task] = weight

def deleteTask(tasks):
    print(tasks)
    task = inputTask()
    del tasks[task]

def randomize(tasks):
    TaskList = []
    for task in tasks:
        for i in range(tasks[task]):
            TaskList.append(task)
    randomTask = random.choice(TaskList)
    return randomTask

def viewList(tasks):
    print("Tasks:")
    for task in tasks:
        print(task)
    

def makeChoice():
    tasks = getTasks()
    if len(sys.argv) > 1:
        number = "1"
    else:
        number = choices()
        print("")
    if number == "1":
        print("Your random task is:")
        task = randomize(tasks)
        print(task)
        print("")
        sys.exit()
    elif number == "2":
        print("Add task")
        addTask(tasks)
        storeTasks(tasks)
    elif number == "3":
        print("Delete task")
        deleteTask(tasks)
        storeTasks(tasks)
    elif number == "4":
        viewList(tasks)
    elif number == "5":
        sys.exit()
    print("")

def main():
    while True:
        makeChoice()

if __name__ == "__main__":
    main()

#sys.argv