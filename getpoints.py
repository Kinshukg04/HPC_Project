import random


def getpoint(val ):
    INTERVAL =val
    circle_points= 0
    square_points= 0

    for i in range(INTERVAL):

        rand_x= random.uniform(-1, 1)
        rand_y= random.uniform(-1, 1)

        origin_dist= rand_x*2 + rand_y*2

        if origin_dist<= 1:
            circle_points+= 1

        square_points+= 1
        
    return circle_points

def comp(circle_points,square_points):
    
    circle_points,square_points =getpoint(10000000)
    pi = 4* circle_points/ square_points
    print("Final Estimation of Pi=", pi)  
    
    return pi

