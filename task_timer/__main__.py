# main
# task-timer
# David Marin
# Last Updated: 2/18/2025
  
import click
import datetime
import json
import rich
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

    # First we check if there is a task already named 'name'.
    # We load the list of dictionaries from the file and loop through to check.
    datalist = load_file()

    for dict in datalist:
        if dict['name'] == name:
            print(f'Sorry, there is already a task with the name "{name}"...')
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

    # First load the list of dictionaries (tasks data, but not objects) from json file.
    # We then search through the dictionaries to see if one matches the name of what task we want to end.
    # If there is a dictionary with our wanted name, we update that dictionary's end_time to the current time,
    # calculate the total_time and update it, and display the end & total time of the task. 
    task_dict_list = load_file()

    for i in range(len(task_dict_list)):
        if task_dict_list[i]['name'] == taskname:
            tasknotfound = False
            task_dict_list[i]['end'] = datetime.datetime.now()
            # format = "%Y-%m-%d %I:%M:%S %p"
            format = "%Y-%m-%dT%H:%M:%S.%f"
            start = datetime.datetime.strptime((task_dict_list[i]['start']), format)
            end = (task_dict_list[i]['end'])
            task_dict_list[i]['total_time'] = str(end - start)

            # Changing dictionary['end'] into a string because "datetime" object is not json serializable
            task_dict_list[i]['end'] = str(task_dict_list[i]['end'])
            save_data(task_dict_list)

    if tasknotfound:
        print(f'Sorry, no task with name "{taskname}" was found...')

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
