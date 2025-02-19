# tasktimer_class
# Author: David Marin
# Last updated: 2/18/2025
#
# usage: from task_class import Task
import datetime
import rich
from rich.console import Console


class Task:
    """ Create a Task class with Task characteristics*. """
    # A Tasktimer object is simply a stopwatch that tracks time when prompted
    # Characteristics of Tasktimer:
    #     * Start/stop time on task
    #     * Display current time task is taking

    def __init__(self, name="Default Task", start_time=0, end_time="Running...", total_time=0):
        """ Initiate a Task class with Task characteristics. """
        # *** Task's timer is started automatically when a Task object is created for efficiency purposes.

        console = Console()

        self.name = name
        self.start_time = datetime.datetime.now()
        self.end_time = "Running..."
        self.total_time = "Running, not determined..."

        # I want a message to display immediately when the task is created
        format = "%Y-%m-%d %I:%M:%S %p"
        console.print(f'Task "{self.name}" created at {(self.start_time).strftime(format)}.', style='yellow4')

    def convert_todict(self):
        """ Return the data of an object in dictionary form for json file input. """
        return {
            "name" : self.name,
            "start" : self.start_time.isoformat(),
            "end" : self.end_time,
            "total_time" : self.total_time,
        }
    
