import random
import matplotlib.pyplot as plt
import numpy as np
#def monte_carlo_pi_part(n):
    
#     count = 0
#     for i in range(n):
#         x=random.random()
#         y=random.random()
        
#         # if it is within the unit circle
#         if x*x + y*y <= 1:
#             count=count+1
        
#     #return
#     return count

def monte_carlo_pi_part(n):
    
    count = 0
    x=[]
    y=[]
    x1=[]
    y1=[]
    for i in range(n):
        rand_x=random.random()
        rand_y=random.random()
        
        # if it is within the unit circle
        if rand_x*rand_x + rand_y*rand_y <= 1:
            count=count+1
            x.append(rand_x)
            y.append(rand_y)
        else:
            x1.append(rand_x)
            y1.append(rand_y)
        
    plt.scatter(x, y,color='r')
    plt.scatter(x1, y1,color='b')
    #plt.show()
    name = './graph'+str(random.random())+'.png'
    plt.savefig(name)
    #return
    return count