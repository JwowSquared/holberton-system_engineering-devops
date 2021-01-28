#!/usr/bin/python3
"""x"""
import json
import requests

if __name__ == "__main__":
    users = requests.get("http://jsonplaceholder.typicode.com/users").json()
    todos = requests.get("http://jsonplaceholder.typicode.com/todos").json()
    out = {}
    tasks = []

    for t in todos:
        tasks.append([t.get("userId"), t.get("title"), t.get("completed")])

    for user in users:
        uname = user.get("username")
        target = user.get("id")
        em = []
        for t in tasks:
            if target == t[0]:
                em.append({"task": t[1], "completed": t[2], "username": uname})
        out.update({str(target): em})

    with open("todo_all_employees.json", "w") as f:
        json.dump(out, f)
