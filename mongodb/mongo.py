import os
import pymongo  # package for working with MongoDB

mongodb_uri = os.getenv('MONGODB_URI', default='mongodb://localhost:27017/')
client = pymongo.MongoClient(mongodb_uri)

#client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["TasksDB"]
tasks = db["tasks"]
tasks_list = []

for n in range(0, 100):
    task = {}
    task["taskname"] = "task " + str(n+1)
    task["sleeptime"] = 60
    task["state"] = "created"
    task["host"] = "slave " + str(n+1)
    tasks_list.append(dict(task))



x = tasks.insert_many(tasks_list)
print(x.inserted_ids)
for x in tasks.find():
    print(x)