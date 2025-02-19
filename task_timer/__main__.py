# main
# task-timer
# David Marin
# Last Updated: 2/18/2025
  
import click
import datetime
import json
import rich
from rich.table import Table
from rich.console import Console
import os
from task_class import Task

jsontasksfile = "tasksfile.json"

@click.group()
def main():
    """ Create a click group for all other functions. """
    pass

def load_file():
    """ Return the loaded data of a json file. """

    if os.path.exists(jsontasksfile):
        
        # Return an empty list if no file exists
        if os.path.getsize(jsontasksfile) == 0:
            return []

        else:    
            with open(jsontasksfile, "r") as f:
                return json.load(f)
        

def save_data(dict_list):
    """ Save the list of dictionaries of a task into a json file. """

    # Argument 'dict_list' should be a list of dictionaries with all of the class's attributes 

    with open(jsontasksfile, "w") as f:
        json.dump(dict_list, f, indent=6)

def dict_to_task(dictionary):
    """ Return a task object with dictionary data. """

    task = Task(name=(dictionary['name']), start_time=(dictionary['start']), end_time=(dictionary['end']), total_time=(dictionary['total_time']))

    return task


@main.command()
@click.argument("name")
def create_task(name):
    """ Create a new task 'Name' using click. """

    console = Console()

    # First we check if there is a task already named 'name'.
    # We load the list of dictionaries from the file and loop through to check.
    datalist = load_file()

    for dict in datalist:
        if dict['name'] == name:
            console.print(f'Sorry, there is already a task with the name "{name}"...', style='red1')
            return

    newtask = Task(name)

    # Immediately save task to a file by first turning task into a dictionary,
    # loading the list of dictionaries from the json file, appending the task's dictionary
    # to that list, and finally saving that list to the json file
    task_dict = newtask.convert_todict()
    datalist.append(task_dict)
    save_data(datalist)

@main.command()
@click.argument('taskname')
def end_task(taskname):
    """ End a task and display total time of said task. """

    # This variable used for errors if task is not found
    tasknotfound = True

    console = Console()

    # First load the list of dictionaries (tasks data, but not objects) from json file.
    # We then search through the dictionaries to see if one matches the name of what task we want to end.
    # If there is a dictionary with our wanted name, we update that dictionary's end_time to the current time,
    # calculate the total_time and update it, and display the end & total time of the task. 
    task_dict_list = load_file()

    for i in range(len(task_dict_list)):
        if task_dict_list[i]['name'] == taskname:
            tasknotfound = False
            task_dict_list[i]['end'] = datetime.datetime.now()
            format = "%Y-%m-%dT%H:%M:%S.%f"
            start = datetime.datetime.strptime((task_dict_list[i]['start']), format)
            end = (task_dict_list[i]['end'])
            task_dict_list[i]['total_time'] = str(end - start)

            console.print(f'Ended task "{task_dict_list[i]['name']}" at {task_dict_list[i]['end']}.', style='red1')

            # Changing dictionary['end'] into a string because "datetime" object is not json serializable
            task_dict_list[i]['end'] = str(task_dict_list[i]['end'])
            save_data(task_dict_list)

    if tasknotfound:
        console.print(f'Sorry, no task with name "{taskname}" was found...', style='red1')


@main.command()
def running_tasks():
    """ Print out each tasks that are running. """

    console = Console()
    task_notfound = True

    # We first load the list of dictionaries with each task's data into a variable.
    # Then we iterate through the dictionaries to find any whose end is 'Running...' and
    # print the contents of the task if it is currently running.
    task_dict_list = load_file()


    for i in range(len(task_dict_list)):
        if task_dict_list[i]['end'] == "Running...":
            task_notfound = False
            console.print(f'\nTask "{task_dict_list[i]['name']}" is currently running: Started at {task_dict_list[i]['start']}.', style='orange1')

    if task_notfound:
        console.print("Sorry, there are no running tasks...", style='red1')

@main.command()
def timesheet():
    """ Print out a timesheet of all tasks. """

    # First load list of dicts with task data into a variable.
    # Then print out all data for each variable.

    task_dict_list = load_file()

    table = Table(title="Task Timesheet")

    table.add_column("Task Name", style="cyan1")
    table.add_column("Start Time", style="green1")
    table.add_column("End Time", style="red1")
    table.add_column("Total Time", style="dark_slate_gray1")

    # Creating a row for each dictionary (task) in the list from json file

    for i in range(len(task_dict_list)):
        table.add_row(f'{task_dict_list[i]['name']}', f'{task_dict_list[i]['start']}', f'{task_dict_list[i]['end']}', f'{task_dict_list[i]['total_time']}')

    console = Console()
    console.print(table)




@main.command()
def edit_timesheet():
    """ Allow user to choose what to edit in timesheet. """

    # Really, the user is just editing the json file which is a list of dictionaries containing
    # the data to all of the tasks. So we create a nice menu to ask the user what they want to edit,
    # then we pass their option into the function that actually edits the timesheet.

    console = Console()
    task_dict_list = load_file()

    # Getting user input for what they want to edit
    console.print("Please enter the name of the task to edit: ", style='dark_violet')
    name = input()

    console.print('\nWhat would you like edit for that task? (Enter cooresponding letter):\n', style='dark_violet')
    console.print('(n)....................... name', style='cyan1')
    console.print('(s)................. start time', style='green1')
    console.print('(e)................... end time', style='red1')
    console.print('(t)................. total time', style='dark_slate_gray1')
    thing2edit = input()

    # Changing thing2edit to correct format for editing
    if thing2edit == 's':
        thing2edit = 'start'
    elif thing2edit == 'e':
        thing2edit = 'end'
    elif thing2edit == 't':
        thing2edit = 'total_time'
    elif thing2edit == 'n':
        thing2edit = 'name'

    console.print(f'\nWhat would you to change it to? (Please enter in correct format. Run timesheet for reference)', style='dark_violet')
    edit = str(input())

    for i in range(len(task_dict_list)):
        if task_dict_list[i]['name'] == name:
            task_dict_list[i][thing2edit] = edit
            save_data(task_dict_list)

if __name__ == '__main__':
    main()
