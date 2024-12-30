Read-me file for Module 1, To Do List Project: Intro, About, How to use

Introduction -
At first, I attempted to go with the import function, as I did with the prework project,
Until I realized, I didn't know how to upload it to github as it being two part.
So, I went a different route, where at the end I used While to prompt the connection.
I'm not sure if this was the correct way to go about it but after hours and hours and hours of going at it
I finally got all functions workings.

About-
The start of the project relies on the empty list.
From there, I began making the functions for each option.
I found the first function, was relatively simple and could simply use try, except, finally
I was able to create the function to append / add tasks to the list.

Second function I needed more than just try, execpt, finally to view the list.
I started it with try, and then went with if not, in case they tried to view with no tasks appended
then else, to view the actual tasks that were appended, and the for loop to cycle them
which I followed up with Except and finally as per the instructions to ensure a backup check.

Third function was to delete tasks, I tried to just copy my formula from the second function.
I started with Try, and worked my way down to if not, and else as I did prior
This is where I got stuck and my brain was fried and could not figure out how to move forward. I guessed and checked
a lot until I took a break do to meltdown. After lunch and break, I came back and tried another if / else /in follow up as I had 
done on a previous saved file and it cleared the way a bit.
I was able to get a better order of operations down by first addressing if not a task to delete, then to follow up with else to enter a task to delete:
if not tasks:
            print("No tasks to delete.")
        else:
            task_to_delete = input("Enter task to delete: ")
            if task_to_delete in tasks:
                tasks.remove(task_to_delete)
                print("Task deleted")
            else:
                print("Task not found")
From this point I was able to add in the checkers of except , finally.
I learned that when deleting anything in code, is likely where errors arise and best for try, except, finally so I made sure to triple check this section before moving on.

4th function was tied into the finale, as I used "While True" to act as my connector to the above functions.
I started with try again and then linked back the main_menu that I used to kick off the program and connected the options to the functions.
Ended it with except and finally for final checks



How to use-
1.Run program.
2.Select an option from the main menu
a.) to add task - asks what type of task you'd like to add. type in anything to add to list.
b.) to view task(s) - gives a list of tasks added from option a, or tells you there are none.
c.) to delete task- asks what type of task you'd like to delete. type in task that was added in from option 1
d.) to quit - ends program
