from getpoints import getpoint
import client
import server 
import multiprocessing
from multiprocessing import Pool
import time

x = int(input("1 for server  , 2 for client ")) 
#host=input("input the host of the server") 

#port=int(input("input the port"))
host='192.168.29.219'
port=36601

if(x==1):
    val=int(input("input the interval")) 
    server.send(host,port,str(val))
    val = val/2
    
    # multiprocessing
    np = multiprocessing.cpu_count()
    print ('You have {0:1d} CPUs'.format(np))
    part_count=[int(val/np) for i in range(np)]
    pool = Pool(processes=np) 
    cp = pool.map(getpoint, part_count)
    cp = sum(cp)
    print("locally computed",cp)
    server.send(host,port,str(cp)) 

else:
    val=int(client.recv(host,port).split('.')[0]) 
    print("interval received" ,val)
    val = val/2
    np = multiprocessing.cpu_count()
    print ('You have {0:1d} CPUs'.format(np))
    part_count=[int(val/np) for i in range(np)]
    pool = Pool(processes=np) 
    cp1 = pool.map(getpoint, part_count)
    cp1 = sum(cp1)
    print("locally computed",cp1)
    cp2=int(client.recv(host,port).split('.')[0])
    print("received",cp2)
    pi = getpoint.comp(cp1+cp2,val)
    print(pi)
    
        
    
    

    
    
