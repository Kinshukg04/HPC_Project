import sys
sys.path.append('../')
from modules.firebase import *
import functions.process
import random
import json
from modules.firebase import *

def getpoint(val):
    INTERVAL = val
    count = 0
    for i in range(INTERVAL):
        x = random.random()
        y = random.random()

        # if it is within the unit circle
        if x*x + y*y <= 1:
            count = count+1

    #return
    return count


def comp(circle_points, interval):

    circle_points = getpoint(interval)
    pi = 4 * circle_points / interval
    #print("Final Estimation of Pi = ", pi)
    return pi


x = 10000000
numberOfdevices = 1

def GetList():
    numberOfdevices= getnums()
    m = functions.process.mulpy()
    input_data = m.splitData(x,numberOfDevices=numberOfdevices,split_type = 'split')
    file_name = 'test.py'
    function_name = 'getpoint'
    multiprocess = False
    jsonData = []
    for user in range(0, numberOfdevices):
        dict = {}
        dict = {'fileName': file_name, 'funcName': function_name, 'input_data': input_data[user],
                'numberOfDevices': 2, 'multiprocess': multiprocess}
        jsonData.append(dict)
    return jsonData

def Process(ele):
    return getpoint(ele['input_data'])

def Combine(lst):
    s = 0
    for i in lst:
        s += i
    print('Estimated pi',4*s/x)

# for host

loginFirebase("123@123.com" ,"123456789")

lst=GetList()
print(lst[1])
distributeprocess(lst)
val = ProcessRequestCheck()
print(val)
val =Process(val)
print(val)
SendOutput(val)
lst= ConbineOutput()
print(lst)
Combine(lst)
exit()

#for client
"""
loginFirebase("1234@1234.com","123456789")
val = ProcessRequestCheck()
print(val)
val =Process(val)
print(val)
SendOutput(val)
exit()
"""

