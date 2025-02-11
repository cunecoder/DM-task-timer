# main
# task-timer
# David Marin
# Last Updated: 1/29/2025
  
import click


# @click.command()
# @click.option('--name')
# def create_task(name):
#     """ Create a new task using click. """
#     print("TEST WORKED")
#     task = Task("First Task")
#     task.display_name()


def question():
    print("What are the chances of this working?")

def answer():
    print("The answer is 100/%/ because I know I can figure this out.")

@click.command()
@click.argument('choice')
@click.option('-createtask', '-ct', help='Create task with inputted name')

def main(choice, createtask):
    """ This is my main cli. """
    #if choice = 'printq':
        #question()
    
    click.echo(f"Testing first; name of your task is {createtask}, but arg is {choice}!")

if __name__ == '__main__':
    main()
