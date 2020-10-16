#!/usr/bin/env python3

# Import of python system libraries.
# These libraries will be used to create the web server.
# You don't have to install anything special, these libraries are installed with Python.
import os
import pymongo
import socket
import threading
import socketserver


class ClientThread(threading.Thread):

    def __init__(self, ip, port, socket):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.socket = socket 
        print("[+] New thread started for " + self.ip + ":" + str(self.port))

    def run(self):    
        print("Connection from : " + self.ip + ":" + str(self.port))
        data = self.socket.recv(2048)
        print("Client sent : ", data.decode())
        data = "\nWelcome to the server\n\n"
        self.socket.send(data.encode())
        print("Client disconnected...")

def startServer():
    host = socket.gethostname()
    print("hostname is: ", host)
    port = 2345
    tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcpsock.bind((host,port))
    threads = []
    while True:
        tcpsock.listen(4)
        print("\nListening for incoming connections...")
        (clientsock, (ip, port)) = tcpsock.accept()
        newthread = ClientThread(ip, port, clientsock)
        newthread.start()
        threads.append(newthread)

    for t in threads:
        t.join()

def connectToMongo():
    client = pymongo.MongoClient("mongodb://root:example@mongo:27017")
    db = client["TasksDB"]
    print("[MASTER] DB is: ", db)

if __name__ == '__main__':
    startServer()

