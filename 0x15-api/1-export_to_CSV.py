#!/usr/bin/python3
"""Gather data from an API and export to CSV"""
import csv
import requests
import sys


if __name__ == "__main__":
    BASE_URL = "https://jsonplaceholder.typicode.com"
    user_id = sys.argv[1]

    todos = requests.get(f"{BASE_URL}/todos?userId={user_id}").json()
    user = requests.get(f"{BASE_URL}/users/{user_id}").json()

    user_name = user.get('username')

    csv_output = [[t.get('userId'), user_name, t.get('completed'),
                   t.get('title')] for t in todos]

    with open(f"{user_id}.csv", "w", newline="") as f:
        write = csv.writer(f, quoting=csv.QUOTE_ALL)
        write.writerows(csv_output)
