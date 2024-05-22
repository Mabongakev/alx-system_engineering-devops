#!user/bin/python3
"""
Write a Python script that uses REST API that returns information about a given employee's completed tasks.
"""

import requests
import sys

def get_employee_todos():
    employee_respose = requests.get(f'https://jsonplaceholder.typicode.com/users{id}')
    if employee_respose.status_code != 200:
        return 'Error: Could not find employee with that ID'
    
    todos_repsonse = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={id}/todos')
    if todos_repsonse.status_code != 200:
        return 'Error: Could not find todos for that employee'
    
    name = employee_respose.json().get('name')

    todos = todos_repsonse.json()
    completed_tasks = [task for task in todos if task.get('completed') is True]
    total_tasks = len(todos_response.json())

    print('Employee {} is done with tasks({}/{}):'.format(name,
          len(completed_tasks), total_tasks))

    for task in completed_tasks:
        print(f"\t {task.get('title')}")

if __name__ == "__main__":
    get_employee_todos(sys.argv[1])
