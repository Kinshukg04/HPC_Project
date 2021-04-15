# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 00:22:58 2021

@author: Jai Kumawat
"""
import random
import matplotlib.pyplot as plt
  
import numpy as np

def getpoint(val ):
    INTERVAL =val
    circle_points= 0
    square_points= 0
    x=[]
    y=[]
    x1=[]
    y1=[]
    for i in range(INTERVAL):

        rand_x= random.uniform(-1, 1)
        rand_y= random.uniform(-1, 1)

        origin_dist= rand_x**2 + rand_y**2

        if origin_dist<= 1:
            circle_points+= 1
            x.append(rand_x)
            y.append(rand_y)
        else:
            x1.append(rand_x)
            y1.append(rand_y)
        square_points+= 1
    plt.scatter(x, y,color='r')
    plt.scatter(x1, y1,color='b')
    plt.show()    
    lst=[circle_points ,square_points]
    return lst
print(getpoint(1000))


  