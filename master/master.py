#!/usr/bin/env python3

# Import of python system libraries.
# These libraries will be used to create the web server.
# You don't have to install anything special, these libraries are installed with Python.
import os
import pymongo
import socket

print("[MASTER] Hi!")

def connectToMongo():
    client = pymongo.MongoClient("mongodb://root:example@mongo:27017")
    db = client["TasksDB"]
    print("[MASTER] DB is: ", db)

def server_program():
    host = socket.gethostname()
    port = 2345
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(2)
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))
    while True:
        data = conn.recv(1024).decode()
        print("[MASTER] ", data)
        if not data:
            break
        data = "Hi from Server"
        conn.send(data.encode())
    conn.close()

connectToMongo()
while True:
    server_program()