import client
import server 
import socket

host= input("ENTER HOST")
port =int(input("ENTER PORT"))

server.send(host,port ,"heyhey")



