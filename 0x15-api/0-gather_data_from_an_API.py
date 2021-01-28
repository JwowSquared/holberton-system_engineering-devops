#!/usr/bin/python3
"""x"""
import requests
from sys import argv

if __name__ == "__main__":
    users = requests.get("http://jsonplaceholder.typicode.com/users").json()
    todos = requests.get("http://jsonplaceholder.typicode.com/todos").json()
    target = int(argv[1])
    employee = ""
    tasks = []
    done = 0
    total = 0

    for user in users:
        if user.get("id") == target:
            employee = user.get("name")
            break

    for task in todos:
        if task.get("userId") == target:
            total += 1
            if task.get("completed"):
            tasks.append(task.get("title"))
                done += 1

    out = "Employee {} is done with tasks({:d}/{:d}):"
    print(out.format(employee, done, total))
    for task in tasks:
        print("\t {}".format(task))
