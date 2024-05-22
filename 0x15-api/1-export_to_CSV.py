#!/usr/bin/python3
# Using what you did in the task #0, extend
# your Python script to export data in the CSV format.

import requests
import sys
import json

def employee_todos_to_csv(id):
    """
    Gets todos belonging to employee with given id
    """

    employee_response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{id}"
    )

    if employee_response.status_code != 200:
        return

    todos_response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{id}/todos")

    if todos_response.status_code != 200:
        return

    name = employee_response.json().get('username')
    todos = todos_response.json()

    csv_data = ""

    for task in todos:
        csv_data += "\"{}\",\"{}\",\"{}\",\"{}\"\n".format(
            id, name, task.get('completed'), task.get('title'))

    with open(f"{id}.csv", "w+") as csvfile:
        csvfile.write(csv_data)


if __name__ == "__main__":
    employee_todos_to_csv(sys.argv[1])
