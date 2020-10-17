import socket
import time
import pickle

def client_program():
    host = "master"
    port = 2345
    client_socket = socket.socket()
    client_socket.connect((host, port))
    
    data = client_socket.recv(1024)
    task = pickle.loads(data)
    sleepTime = task["sleeptime"]
    clientId = task["_id"]
    taskName = task["taskname"]

    print("[" + str(clientId) + "] " + str(taskName) + "Task received from server.")
    time.sleep(sleepTime)
    print("[ " + str(clientId) + " ]" + str(taskName) + "Task completed.")

    response = {"clientId": str(clientId), "status": "success"}
    client_socket.send(pickle.dumps(response))
    client_socket.close()


if __name__ == '__main__':
    time.sleep(5)
    client_program()
