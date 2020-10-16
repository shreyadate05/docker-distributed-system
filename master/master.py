#!/usr/bin/env python3

# Import of python system libraries.
# These libraries will be used to create the web server.
# You don't have to install anything special, these libraries are installed with Python.
import os
import pymongo
import http.server
import socketserver


print("[MASTER] Hi!")

client = pymongo.MongoClient("mongodb://root:example@mongo:27017")
db = client["TasksDB"]
print("[MASTER] DB is: ", db)


handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", 1234), handler) as httpd:
    httpd.serve_forever()

