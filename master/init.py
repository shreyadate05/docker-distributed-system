#!/usr/bin/env python3

# Import of python system libraries.
# These libraries will be used to create the web server.
# You don't have to install anything special, these libraries are installed with Python.
import os
import pymongo

print("[INIT] Connecting to TasksDB")

client = pymongo.MongoClient("mongodb://root:example@mongo:27017")
db = client["TasksDB"]
tasks = db["tasks"]
tasks_list = []

print("[INIT] Inserting 100 tasks in TasksDB")
for n in range(0, 100):
    task = {}
    task["taskname"] = "task " + str(n+1)
    task["sleeptime"] = 60
    task["state"] = "created"
    task["host"] = "slave " + str(n+1)
    tasks_list.append(dict(task))

x = tasks.insert_many(tasks_list)
print("[INIT] Inserted 100 tasks in TasksDB")
