
import client
import server 
import socket

host= input("ENTER HOST")
port =int(input("ENTER PORT"))

print(client.recv(host,port ))
