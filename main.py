import json
import os
from tasks_handler import tasksHandler
from typing import List, Dict, Optional, Union
TASKS_HANDLER = None
AVAILABLE_TASKS: List[str] = []
CONFIG: Union[Dict] = None


def get_available_tasks() -> List[str]:
    """
    Getting a list of all the available tasks
    """
    options: List[str] = tasksHandler.__dir__(TASKS_HANDLER)
    results: List[str] = []
    for method in options:
        if not method.startswith("__"):
            results.append(method)
    return results


def get_tasks_prompt() -> int:
    """
    Generating the prompt of the available tasks
    """
    global AVAILABLE_TASKS
    AVAILABLE_TASKS = get_available_tasks()
    prompt = "Please insert desired task index:"
    for index, option in enumerate(AVAILABLE_TASKS):
        task_description = ""
        if option in CONFIG and "desc" in CONFIG[option]:
            task_description = CONFIG[option]["desc"]
        prompt += f"\n {index + 1}. {option}: {task_description}"
    return int(input(prompt + "\n\n"))


def init_config(config_path: str = "config.json") -> None:
    """
    Init the configuration file - default path: './config.json'
    """
    global CONFIG
    if os.path.isfile(config_path):
        with open(config_path) as content:
            CONFIG = json.load(content)
    else:
        raise Exception(
            "[ERROR] - Could not init config file: No such file or directory.")


def get_task_config(task_name: str) -> Union[Dict]:
    """
    Getting the list of arguments of the chosen task from config.json
    """
    if task_name in CONFIG.keys():
        return CONFIG[task_name]
    return None


def main():
    chosen_index = get_tasks_prompt()
    if chosen_index > len(AVAILABLE_TASKS):
        raise Exception("Non existed method has been chosen!")
    chosen_task = AVAILABLE_TASKS[chosen_index - 1]
    task_config = get_task_config(chosen_task)
    if task_config and "args" in task_config:
        args = task_config["args"]
        print(f"Executing automatic preview run with sent arguments: {args}")
        result = getattr(
            TASKS_HANDLER, chosen_task)(*args)
        print(f"results are: {result}")
    else:
        result = getattr(TASKS_HANDLER, chosen_task)()
        print(f"results are: {result}")
    return result


if __name__ == "__main__":
    TASKS_HANDLER = tasksHandler()
    init_config()
    main()
