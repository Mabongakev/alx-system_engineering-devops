
#!/usr/bin/python3

"""
Write a Python script that, using this REST API,
for a given employee ID, returns information
about his/her TODO list progress.

Requirements:

    - You must use urllib or requests module
    - The script must accept an integer as a parameter,
      which is the employee ID
    - The script must display on the standard
      output the employee TODO list progress in this exact format:
        - First line: Employee EMPLOYEE_NAME is done with
        tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
            - EMPLOYEE_NAME: name of the employee
            - NUMBER_OF_DONE_TASKS: number of completed tasks
            - TOTAL_NUMBER_OF_TASKS: total number of tasks,
            which is the sum of completed and non-completed tasks
        - Second and N next lines display the title
          of completed tasks: TASK_TITLE
          (with 1 tabulation and 1 space before the TASK_TITLE)
"""

import requests
import sys


def get_employee_todos(id):
    employee_response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{id}"
    )

    if employee_response.status_code != 200:
        return

    todos_response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{id}/todos")

    if todos_response.status_code != 200:
        return

    name = employee_response.json().get('name')

    todos = todos_response.json()
    completed_tasks = [task for task in todos if task.get('completed') is True]
    total_tasks = len(todos_response.json())

    print('Employee {} is done with tasks({}/{}):'.format(name,
          len(completed_tasks), total_tasks))

    for task in completed_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    get_employee_todos(sys.argv[1])
