import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def conn(host ,port):
    s.bind((host, port))
    s.listen(5)
    
def send(message):   
    while True:
        # now our endpoint knows about the OTHER endpoint.
        clientsocket, address = s.accept()
        print(f"Connection from {address} has been established.")
        clientsocket.send(bytes(message,"utf-8"))
        clientsocket.close()
        print("sent , now terminating")
        break
    
    
