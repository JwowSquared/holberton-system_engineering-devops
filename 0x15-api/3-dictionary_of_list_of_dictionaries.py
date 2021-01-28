#!/usr/bin/python3
"""x"""
import json
import requests

if __name__ == "__main__":
    users = requests.get("http://jsonplaceholder.typicode.com/users").json()
    todos = requests.get("http://jsonplaceholder.typicode.com/todos").json()
    out = {}

    for user in users:
        username = user.get("username")
        target = user.get("id")
        tasks = {}
        for task in todos:
            if task.get("id") == target:
                tasks.update({task.get("title"): task.get("completed")})
        emp = []
        for t, c in tasks.items():
            emp.append({"task": t, "completed": c, "username": username})
        out.update({str(target): emp})

    with open("todo_all_employees.json", "w") as f:
        json.dump(out, f)
