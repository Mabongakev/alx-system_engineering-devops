#!usr/bin/python3
"""
Write a Python script that uses REST API that returns information about a given employee's completed tasks.
"""

import requests
import sys
import json

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
