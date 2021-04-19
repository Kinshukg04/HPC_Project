import random


def getpoint(val):
    INTERVAL =val
    count = 0
    for i in range(INTERVAL):
        x=random.random()
        y=random.random()
        
        # if it is within the unit circle
        if x*x + y*y <= 1:
            count=count+1
        
    #return
    return count

def comp(circle_points,interval):
    
    circle_points = getpoint(interval)
    pi = 4* circle_points/ interval
    #print("Final Estimation of Pi = ", pi)  
    return pi

