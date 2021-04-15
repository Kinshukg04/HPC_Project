import getpoints
import client
import server 

x = input("1 for server  , 2 for client ") 
host=input("input the target host") 
port=input("input the target port")

if(x==1):
    val=input("input the interval") 
    
    server.send(host,port,val)
    cp = getpoints.getpoints(val/2) 
    server.send(host,port,cp) 

else:
    val=int(client.recv(host,port)) 
    cp1 = getpoints.getpoints(val/2) 
    cp2=int(client.recv(host,port))
    pi = getpoints.comp(cp1+cp2,val)
    print(pi)
    
        
    
    
