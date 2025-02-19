# tasktimer_class
# Author: David Marin
# Last updated: 2/6/2025
#
# usage: from task_class import Task
import datetime


class Task:
    """ Create a Task class with Task characteristics*. """
    # A Tasktimer object is simply a stopwatch that tracks time when prompted
    # Characteristics of Tasktimer:
    #     * Start/stop time on task
    #     * Display current time task is taking

    def __init__(self, name="Default Task", start_time=0, end_time="Running...", total_time=0):
        """ Initiate a Task class with Task characteristics. """
        # *** Task's timer is started automatically when a Task object is created for efficiency purposes.

        self.name = name
        self.start_time = datetime.datetime.now()
        self.end_time = "Running..."
        self.total_time = 0

        # I want a message to display immediately when the task is created
        format = "%Y-%m-%d %I:%M:%S %p"
        print(f'Task "{self.name}" created at {(self.start_time).strftime(format)}.')

    def end_task(self):
        """ End the 'stopwatch' for task and update total time. """
        # Record time that task ends
        self.end_time = datetime.datetime.now()

        # Format string for time manipulation and printing
        format = "%Y-%m-%d %I:%M:%S %p"

        # Updating total_time based on task's beginning and ending time
        start = (self.start_time).strftime(format)
        end   = (self.end_time).strftime(format)
        self.total_time = (datetime.datetime.strptime(end, format)) - self.start_time
        
        # Displaying duration of task
        print(f'Task "{self.name}" ended at {self.end_time}. Total duration: {self.total_time}.')

    def convert_todict(self):
        """ Return the data of an object in dictionary form for json file input. """
        return {
            "name" : self.name,
            "start" : self.start_time.isoformat(),
            "end" : self.end_time,
            "total_time" : self.total_time,
        }

    def display_time(self):
        """ Display the total_time of a task. """
        print(f'The total time for {self.name} is: {self.total_time}')


    def display_name(self):
        """ Display task's name. """
        print(self.name)


    def create_dictionary(self):
        """ Store the data of the object in a dictionary. """

        my_dict = {
            "name" : self.name, 
            "start_time" :  str(self.start_time), 
            "end_time" : self.end_time,
            "total_time" : self.total_time
        }

        return my_dict
