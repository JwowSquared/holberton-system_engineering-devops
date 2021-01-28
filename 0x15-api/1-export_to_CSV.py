#!/usr/bin/python3
"""x"""
from csv import DictWriter, QUOTE_ALL
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

    with open("{}.csv".format(target), "w") as f:
        for title, completed in tasks.items():
            out = {}
            vals = [target, username, completed, title]
            for i in range(len(vals)):
                out.update({fields[i]: vals[i]})
            writer = DictWriter(f, fieldnames=fields, quoting=QUOTE_ALL)
            writer.writerow(out)
