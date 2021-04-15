
import client
import server 
import socket

host= input("ENTER HOST")
port =input("ENTER PORT")

print(client.recv(host,port ))
