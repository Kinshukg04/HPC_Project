from getpoints import getpoint
import client
import server 
import multiprocessing
from multiprocessing import Pool
import time

x = input("1 for server  , 2 for client ") 
host=input("input the target host") 
port=input("input the target port")

if(x==1):
    val=input("input the interval") 
    val = val/2
    server.send(host,port,val)
    # multiprocessing
    np = multiprocessing.cpu_count()
    print ('You have {0:1d} CPUs'.format(np))
    part_count=[int(val/np) for i in range(np)]
    pool = Pool(processes=np) 
    cp = pool.map(getpoint, part_count)
    cp = sum(cp)

    server.send(host,port,cp) 

else:
    val=int(client.recv(host,port)) 
    val = val/2
    np = multiprocessing.cpu_count()
    print ('You have {0:1d} CPUs'.format(np))
    part_count=[int(val/np) for i in range(np)]
    pool = Pool(processes=np) 
    cp1 = pool.map(getpoint, part_count)
    cp1 = sum(cp1)
    cp2=int(client.recv(host,port))
    pi = getpoints.comp(cp1+cp2,val)
    print(pi)
    
        
    
    
