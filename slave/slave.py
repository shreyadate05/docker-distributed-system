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
    print('Received from server: ', task)
    client_socket.close()


if __name__ == '__main__':
    time.sleep(5)
    client_program()