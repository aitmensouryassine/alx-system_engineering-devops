#!/usr/bin/python3
"""Gather data from an API"""
import requests
import sys

if __name__ == "__main__":
    BASE_URL = "https://jsonplaceholder.typicode.com"
    user_id = sys.argv[1]

    todos = requests.get(f"{BASE_URL}/todos?userId={user_id}").json()
    user = requests.get(f"{BASE_URL}/users/{user_id}").json()

    NAME = user.get('name')
    DONE = [todo for todo in todos if todo.get('completed') is True]

    print(f"Employee {NAME} is done with tasks({len(DONE)}/{len(todos)}):")
    for todo in DONE:
        print(f"\t {todo.get('title')}")
