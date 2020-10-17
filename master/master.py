#!/usr/bin/env python3

# Import of python system libraries.
# These libraries will be used to create the web server.
# You don't have to install anything special, these libraries are installed with Python.
import os
import pymongo
import socket
import threading
import socketserver
import pickle
import time

class ClientThread(threading.Thread):

    def __init__(self, ip, port, socket):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.socket = socket 
        self.client = pymongo.MongoClient("mongodb://root:example@mongo:27017")
        self.db = self.client["TasksDB"]
        self.tasks = self.db.tasks
        time.sleep(3)
        print()
        print("[+] New thread started for " + self.ip + ":" + str(self.port))

    def run(self): 
        taskName = ""
        try:
            data = self.tasks.find_one_and_update({"state":"created"}, {"$set": {"state" : "running"}})
            print("data is: ", data)
            taskName = data["taskname"]
            self.socket.send(pickle.dumps(data))
            print("[MASTER |  " +  str(threading.get_ident()) + "] " + taskName + " assigned to slave ")

            listen = True
            while listen:
                status = self.socket.recv(2048)
                if status:
                    listen = False
                    clientStatus = pickle.loads(status)
                    print("[MASTER |  " +  str(threading.get_ident()) + "] " + "Response sent by slave: " + str(clientStatus))
                    if clientStatus["status"] == "success":
                        print("[MASTER |  " +  str(threading.get_ident()) + "] " + taskName + " completed by slave ")
                        data = self.tasks.find_one_and_update({"taskname":taskName}, {"$set": {"state" : "success"}})
        
        except socket.timeout:
            print("[MASTER |  " +  str(threading.get_ident()) + "] " + " Task incomplete due to timeout.")
            data = self.tasks.find_one_and_update({{"taskname":taskName}}, {"$set": {"state" : "killed"}})
        
        except Exception as e:
            print("[MASTER |  " +  str(threading.get_ident()) + "] " + " Task incomplete due to exception: ", e)
            data = self.tasks.find_one_and_update({{"taskname":taskName}}, {"$set": {"state" : "killed"}})

def startServer():
    host = socket.gethostname()
    port = 2345
    tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcpsock.bind((host,port))
    threads = []
    while True:
        tcpsock.listen()
        (clientsock, (ip, port)) = tcpsock.accept()
        newthread = ClientThread(ip, port, clientsock)
        newthread.start()
        threads.append(newthread)

    for t in threads:
        t.join()

if __name__ == '__main__':
    startServer()

