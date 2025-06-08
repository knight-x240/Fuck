import socket
import threading

HOST = input("Enter server IP address: ")
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == "USERNAME":
                client.send(input("Choose a username: ").encode('utf-8'))
            else:
                print(message)
        except:
            print("[Error] Connection closed.")
            client.close()
            break

def write():
    while True:
        msg = input()
        if msg == "/quit":
            client.close()
            break
        client.send(msg.encode('utf-8'))

receive_thread = threading.Thread(target=receive)
write_thread = threading.Thread(target=write)

receive_thread.start()
write_thread.start()
              
