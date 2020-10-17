import socket
import time
import pickle

def client_program():
    host = "master"
    port = 2345

    client_socket = socket.socket()
    try:
        client_socket.connect((host, port))

        data = client_socket.recv(1024)
        task = pickle.loads(data)
        sleepTime = task["sleeptime"]
        clientId = task["_id"]
        taskName = task["taskname"]
        
        print("[" + str(clientId) + "] " + str(taskName) + " received from server.")
        time.sleep(sleepTime)
        print("[ " + str(clientId) + " ]" + str(taskName) + " completed.")
        print("[ " + str(clientId) + " ] Sending \'success\' to server.")

        response = {"clientId": str(clientId), "status": "success"}
        client_socket.send(pickle.dumps(response))

    except Exception as e:
        print("Exception caught: ", e)

    client_socket.close()


if __name__ == '__main__':
    time.sleep(5)
    client_program()
