# This code explains how to create a socket object to create a server
import socket
import threading


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#  set up an IP and port number to the socket
ip = "169.254.230.199"
# print(ip)
port = 1234
# Bind the IP and the port to the socket object 's'
server.bind(('', port))
server.listen(3)

clients = []

# send message to all clients.
def broadcast(message):
    for client in clients:
        client.send(message)

#Get message from a client and broadcast it to the rest
def handle(client):
    while True:
        try:
            message=client.recv(1024)
            broadcast(message)
        except:
            index= clients.index(client)
            clients.remove(client)
            client.close()
            print(f"{client} left the chat due to failure\n")
            break

#accept a new client to the server
def receive():
    while True:
        client, address=server.accept()
        print(f"connected with address {str(address)}")
        #  bytes (string , encoding method)
        message = bytes("what's up client!\n", 'utf-8')
        # send message to the client "client"
        client.send(message)
        clients.append(client)

        broadcast(f"client {clients.index(client)+1} joined the party!\n".encode('utf-8'))
        client.send("welcome aboard!\n".encode('utf-8'))

        thread1= threading.Thread(target=handle,args=(client,))
        thread1.start()

print("Server is listening...")
#loop in an infinite loop to wait for a client to join.
receive()







#
# while 1:
#     # wait for a client to connect
#     client, address = s.accept()
#     print(f"one device is connected with address {address}")
#     #  bytes (string , encoding method)
#     message = bytes("Hello World", 'utf-8')
#     # send message to the client "client"
#     client.send(message)
#     # receive from the client "client"
#     message2 = client.recv(1024)
#     print(message2.decode())
#     # close the connection of the client "client"
#     client.close()
