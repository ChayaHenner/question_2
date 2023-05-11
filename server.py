
import sqlite3
import socket

conn = sqlite3.connect('Employees.db')
c = conn.cursor()
c.execute






server_socket =socket.socket(socket.AF_INET ,socket.SOCK_STREAM)
PORT=1234 #?
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind(('127.0.0.1',PORT)) #ip ,port
server_socket.listen() #unlimited
while True:
    print("server waiting for connection...")
    client_socket,add=server_socket.accept()
    print("client connected from",add)
   
    while True:
        request=client_socket.recv(1024)
        
        #client_socket.send(buf)
