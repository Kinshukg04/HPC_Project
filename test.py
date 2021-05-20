import functions.process
import random
import json

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
numberOfdevices = 2
firebaseConfig = {
    "apiKey": "AIzaSyC8u9ocZsnDeNqRR-j4e7GJfazS558gw-c",
    "authDomain": "hpc-procect-2021.firebaseapp.com",
    "databaseURL": "https://hpc-procect-2021-default-rtdb.firebaseio.com/",
    "projectId": "hpc-procect-2021",
    "storageBucket": "hpc-procect-2021.appspot.com",
    "messagingSenderId": "716203312467",
    "appId": "1:716203312467:web:28809fd0b1668af9e0cda6",
    "measurementId": "G-E4SM5CMNFP"
}

m = functions.process.mulpy(firebaseConfig=firebaseConfig)
data = m.splitData(x,numberOfDevices=numberOfdevices,split_type = 'split')
input_data = []
for i in range(numberOfdevices):
    input_data.append(data[i])
file_name = 'test.py'
function_name = 'getpoint'
multiprocess = False
jsonData = []
for user in range(0, 2):
    dict = {}
    dict = {'fileName': file_name, 'funcName': function_name, 'input_data': input_data[user],
            'numberOfDevices': 2, 'multiprocess': multiprocess}
    jsonData.append(dict)
temp = json.dumps(jsonData)
x = json.loads(temp)
s = 0
for i in input_data:
    s += getpoint(i)
print('Estimated pi',4*s/10000000)
