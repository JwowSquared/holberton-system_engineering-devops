#!/usr/bin/python3
"""x"""
from csv import
import requests
from sys import argv

if __name__ == "__main__":
    users = requests.get("http://jsonplaceholder.typicode.com/users").json()
    todos = requests.get("http://jsonplaceholder.typicode.com/todos").json()
    fields = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
    target = int(argv[1])
    username = ""
    tasks = {}

    for user in users:
        if user.get("id") == target:
            username = user.get("username")
            break

    for task in todos:
        if task.get("userId") == target:
            tasks.update({task.get("title"): task.get("completed")})

    out = []
    for t, c in tasks.items():
        out.append({"task": t, "completed": c, "username": username})

    with open("{}.json".format(target), "w") as f:
        json.dump({argv[1]: out}, f)
