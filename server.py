import socket

def send(host,port,message):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(5)
    
    while True:
        # now our endpoint knows about the OTHER endpoint.
        clientsocket, address = s.accept()
        print(f"Connection from {address} has been established.")
        clientsocket.send(bytes(message,"utf-8"))
        clientsocket.close()
        break
