# This code explains how to create a socket object to create a client
import socket
import threading
import serial

ser = serial.Serial()

ser.port = 'COM6' #from device manager ports (COM & ..)

ser.baudrate = 115200   #same as microcontroller

#ser.open()          #start connection with port (only one client should connect)
# AF_Inet for IPV4 and SOCK_STREAM for TCP/IP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# write the server IP and port number
ip = '127.0.0.1' #server ip
port = 1234
client.connect((ip, port))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            print(message)
            if message[-7:] == 'mnawar\n':
                ser.write(bytearray('y','ascii'))
                
        except:
            print("An Error occured!")
            client.close()
            break

def write():
    while True:
        message = f'ahmed:{input("")}\n'
        client.send(message.encode('utf-8'))

receive_thread=threading.Thread(target=receive)
receive_thread.start()

write_thread=threading.Thread(target=write)
write_thread.start()


