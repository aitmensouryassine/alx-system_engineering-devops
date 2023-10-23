#!/usr/bin/python3
"""Gather data from an API and export to CSV"""
import json
import requests
import sys


if __name__ == "__main__":
    BASE_URL = "https://jsonplaceholder.typicode.com"
    user_id = sys.argv[1]

    todos = requests.get(f"{BASE_URL}/todos?userId={user_id}").json()
    user = requests.get(f"{BASE_URL}/users/{user_id}").json()

    user_name = user.get('username')

    json_output = {user_id: [{"task": todo.get("title"),
                              "completed": todo.get("completed"),
                              "username": user_name} for todo in todos]}

    with open(f"{user_id}.json", "w") as f:
        json.dump(json_output, f)
