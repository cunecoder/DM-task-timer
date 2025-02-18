# main
# task-timer
# David Marin
# Last Updated: 2/18/2025
  
import click
import json
import rich
from task_class import Task

jsontasksfile = "tasksfile.json"

@click.group()
def main():
    """ Create a click group for all other functions. """
    pass

def save_task():
    """ Save each tasks to json file. """
    with open(jsontasksfile, 'w') as jsonfile:
        for task in tasks:
            json.dump(task.create_dictionary(), jsonfile, indent=6)


@main.command()
@click.argument("name")
def create_task(name):
    """ Create a new task using click. """

    # Making sure no duped tasks
    for task in tasks:
        if task.name == task_name:
            console.print("Task name taken.")
            return
        
    newtask = Task(name)

    # Immediately save task to a file
    save_task(newtask)



def access_task():
    """ Load tasks from json file into tasks list. """
    with open(jsontasksfile, 'r') as jsonfile:
        tasks_dictionarys = json.load(jsonfile)
        return [Task.from_dictionary(task_dictionary) for task_dictionary in tasks_dictionarys]
    
    return []

# Updating the task array
# tasks = access_task()

@main.command()
@click.argument('taskname')
def end_task(taskname):
    """ End a task and display total time of said task. """

    print(f'Tasks right now: {tasks}')

    for task in tasks:
        if task.name == 'taskname':
            task.end_task()
            # Save task to file for later usage
            save_task()
            



@main.command()
def answer():
    print("The answer is 100% because I know I can figure this out.")



# @click.command()
# @click.argument('choice')
# @click.option('-createtask', '-ct', help='Create task with inputted name')
# def main(choice, createtask):
#     """ This is my main cli. """
#     #if choice = 'printq':
#         #question()
    
#     click.echo(f"Testing first; name of your task is {createtask}, but arg is {choice}!")

if __name__ == '__main__':
    main()
