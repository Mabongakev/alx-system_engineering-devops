#!/usr/bin/python3

"""
Using what you did in the task #0, extend your Python script
to export data in the CSV format.

Requirements:
    - Records all tasks that are owned by this employee
    - Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
    - File name must be: USER_ID.csv
"""

import json
import requests
import sys


def employee_todos_to_json():
    """
    Gets todos belonging to employee with given id
    """

    json_data = {}

    for i in range(1, 11):
        employee_response = requests.get(
            f"https://jsonplaceholder.typicode.com/users/{i}"
        )

        if employee_response.status_code != 200:
            return

        todos_response = requests.get(
            f"https://jsonplaceholder.typicode.com/users/{i}/todos")

        if todos_response.status_code != 200:
            return

        name = employee_response.json().get('username')
        todos = todos_response.json()

        tasks_list = [{"username": name, "task": task.get(
            'title'), "completed": task.get('completed')} for task in todos]

        json_data[i] = tasks_list

    with open("todo_all_employees.json", "w+") as json_file:
        json.dump(json_data, json_file)


if __name__ == "__main__":
    employee_todos_to_json()
