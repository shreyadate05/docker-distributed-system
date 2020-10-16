import socket
import time

def client_program():
    host = "master"
    port = 2345
    client_socket = socket.socket()
    client_socket.connect((host, port))
    data = "Hi from Client"
    client_socket.send(data.encode())
    data = client_socket.recv(1024).decode()
    print('Received from server: ' + data)
    client_socket.close()


if __name__ == '__main__':
    time.sleep(5)
    client_program()