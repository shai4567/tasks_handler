import json
from tasks_handler import tasksHandler
from typing import List, Dict, Optional, Union
TASKS_HANDLER = None
AVAILABLE_TASKS: List[str] = []


def get_available_tasks() -> List[str]:
    options: List[str] = tasksHandler.__dir__(TASKS_HANDLER)
    results: List[str] = []
    for method in options:
        if not method.startswith("__"):
            results.append(method)
    return results


def get_tasks_prompt() -> int:
    global AVAILABLE_TASKS
    AVAILABLE_TASKS = get_available_tasks()
    prompt = "Please insert desired task index:"
    for index, option in enumerate(AVAILABLE_TASKS):
        prompt += f"\n {index + 1}. {option}"
    return int(input(prompt + "\n\n"))


def get_task_config(task_name: str):
    """
    Getting the list of arguments of the chosen task from config.json
    """
    config: Union[Dict] = None
    with open("config.json") as content:
        config = json.load(content)
    if task_name in config.keys():
        return config[task_name]
    return None


def main():
    # 2. README
    chosen_index = get_tasks_prompt()
    if chosen_index > len(AVAILABLE_TASKS):
        raise Exception("Non existed method has been chosen!")
    task_config = get_task_config(AVAILABLE_TASKS[chosen_index - 1])
    if task_config:
        args = task_config["args"]  # todo check for args using config-file
        result = getattr(
            TASKS_HANDLER, AVAILABLE_TASKS[chosen_index - 1])(*args)
    else:
        result = getattr(TASKS_HANDLER, AVAILABLE_TASKS[chosen_index - 1])()
    return result


if __name__ == "__main__":
    TASKS_HANDLER = tasksHandler()
    main()
