# Tasks and exercises automatic runner tool:
## Agenda:
This is an exercises managment tool.  
Using this tool you can manage , debug and run and all of your python exercises and tasks generically,  
and also keep them all saved under one place.
Using this tool you will eventually have all of your python tasks and solutions to them managed 

## Usage:
The core concept of the usage is separated into 2 main files:

### Tasks Handler file:
The tasks handler files is your playground.  
Here you will write , test and debug your task.  
Simply add a new method into the class and solve your exercise = for example:  
```python
def task1(self, arg1, arg2) -> int:
        # Task 1 solution in here - for example sample task to summarize 2 numbers
        print(f"This task will return the summary of: {arg1} , {arg2}")
        return arg1 + arg2
```  
In this example we defined a simple task to add two sent arguments
We can run the code and also debug it from outside the class scope until we get into a desired solution.  

### The config file:
The bank of the configurations and metadata of our project!  
In this file we will define any additional data we desire to add related to each task.  
For example in our task we want to execute a method that requires 2 arguments to be sent into ,  
We can also add a description for each task (Basically recommended to write what the task was):

```json
{
    "task1": {
        "args": [20, 35],
        "desc": "Return the summary of 2 sent numbers"
    }
}
```

Each config key is related to a solution function, in this example we configured 2 arguments for an automatic dry run of the method "func1".  
We also configured a description that holding the task itself (What the task was)

### The main file:
When the workflow is done , all you have to do is to execute main.py with python3 in order to see prompt of automatic manager of all of your previous tasks and exercises
