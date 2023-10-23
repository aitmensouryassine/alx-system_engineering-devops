#!/usr/bin/python3
"""Gather data from an API and export to CSV"""
import json
import requests


if __name__ == "__main__":
    BASE_URL = "https://jsonplaceholder.typicode.com"

    users = requests.get(f"{BASE_URL}/users").json()

    json_output = {user.get("id"): [{"username": user.get("username"),
                                     "task": todo.get("title"),
                                     "completed": todo.get("completed")}
                                    for todo in requests.get(f"{BASE_URL}/\
todos?userId={user.get('id')}").json()] for user in users}

    with open("todo_all_employees.json", "w") as f:
        json.dump(json_output, f)
